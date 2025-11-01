# train_trend_model.py
import os
import pandas as pd
import numpy as np
from glob import glob
from datetime import timedelta
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import TimeSeriesSplit, GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Optional: use ta (technical analysis) library for indicators
try:
    import ta
except Exception:
    ta = None
    print("ta library not found; some indicators implemented manually. Install 'ta' for more features.")

# --------- USER PARAMETERS ----------
CSV_FILES = ["ADANI_PORT.csv", "AXIS_BANK.CSV", "BAJAJ_FINACE.csv"]  # place files in same folder or give paths
DATE_COL = "Date"
TARGET_UP_THRESHOLD = 0.002   # 0.2% up
TARGET_DOWN_THRESHOLD = -0.002 # -0.2% down
TEST_YEAR = 2022  # use data from this year onward as test (or use last N days)
MODEL_OUT = "rf_trend_model.joblib"
SAMPLE = False  # set True to run faster on subset for quick tests
# ------------------------------------

def load_and_concat(files):
    dfs = []
    for f in files:
        if not os.path.exists(f):
            print(f"File not found: {f} — please put CSVs in script folder or update paths.")
            continue
        df = pd.read_csv(f)
        # normalize column names
        df.columns = [c.strip() for c in df.columns]
        # parse date
        df[DATE_COL] = pd.to_datetime(df[DATE_COL], dayfirst=False, errors='coerce')
        # try to infer ticker from filename
        ticker = os.path.splitext(os.path.basename(f))[0].upper()
        df['Ticker'] = ticker
        dfs.append(df)
    if not dfs:
        raise FileNotFoundError("No CSVs loaded. Check file names/paths.")
    big = pd.concat(dfs, ignore_index=True)
    big = big.sort_values(['Ticker', DATE_COL]).reset_index(drop=True)
    return big

def basic_features(df):
    # Ensure numeric columns exist
    for col in ['Open','High','Low','Close','Adj Close','Volume','VWAP']:
        if col not in df.columns:
            # create placeholder
            df[col] = np.nan
    # Use 'Close' as price
    df['Close'] = df['Close'].astype(float)
    df['Open'] = df['Open'].astype(float)
    df['High'] = df['High'].astype(float)
    df['Low'] = df['Low'].astype(float)
    df['Volume'] = pd.to_numeric(df['Volume'], errors='coerce').fillna(0)
    # daily return
    df['Return'] = df.groupby('Ticker')['Close'].pct_change()
    # log return
    df['LogRet'] = np.log(df['Close']) - np.log(df.groupby('Ticker')['Close'].shift(1))
    # price-based features
    df['HL_range'] = (df['High'] - df['Low']) / df['Low']
    df['OC_change'] = (df['Close'] - df['Open']) / df['Open']
    # rolling features per ticker
    for win in [3,5,10,20]:
        df[f'ma_{win}'] = df.groupby('Ticker')['Close'].transform(lambda x: x.rolling(window=win, min_periods=1).mean())
        df[f'std_{win}'] = df.groupby('Ticker')['Close'].transform(lambda x: x.rolling(window=win, min_periods=1).std())
        df[f'volume_ma_{win}'] = df.groupby('Ticker')['Volume'].transform(lambda x: x.rolling(window=win, min_periods=1).mean())
    # VWAP if present can be used; otherwise make a proxy
    if 'VWAP' in df.columns and df['VWAP'].notna().any():
        df['VWAP'] = pd.to_numeric(df['VWAP'], errors='coerce')
    else:
        # approximate VWAP by typical price * volume rolling average (not exact but fine)
        df['typ_price'] = (df['High'] + df['Low'] + df['Close']) / 3
        df['VWAP'] = df.groupby('Ticker').apply(lambda g: (g['typ_price'] * (g['Volume']+1)).rolling(10, min_periods=1).mean() / (g['Volume']+1).rolling(10, min_periods=1).mean()).reset_index(level=0, drop=True)
    # lag features
    for lag in [1,2,3,5]:
        df[f'close_lag_{lag}'] = df.groupby('Ticker')['Close'].shift(lag)
        df[f'return_lag_{lag}'] = df.groupby('Ticker')['Return'].shift(lag)
    # RSI (simple implementation)
    def compute_rsi(s, window=14):
        delta = s.diff()
        up = delta.clip(lower=0)
        down = -1 * delta.clip(upper=0)
        ma_up = up.rolling(window=window, min_periods=1).mean()
        ma_down = down.rolling(window=window, min_periods=1).mean()
        rs = ma_up / (ma_down + 1e-9)
        return 100 - (100 / (1 + rs))
    df['rsi_14'] = df.groupby('Ticker')['Close'].transform(lambda x: compute_rsi(x, 14))
    return df

def create_target(df, up_th=TARGET_UP_THRESHOLD, down_th=TARGET_DOWN_THRESHOLD):
    # next-day return per ticker
    df['next_close'] = df.groupby('Ticker')['Close'].shift(-1)
    df['next_return'] = (df['next_close'] - df['Close']) / df['Close']
    def labeler(r):
        if pd.isna(r):
            return np.nan
        if r > up_th:
            return 'Up'
        elif r < down_th:
            return 'Down'
        else:
            return 'Neutral'
    df['Trend'] = df['next_return'].apply(labeler)
    return df

def preprocess(df):
    # drop rows with NaN target
    df = df.dropna(subset=['Trend'])
    # drop rows with too many NaNs
    df = df.dropna(thresh=5)  # keep rows with at least 5 non-nulls
    return df

def prepare_X_y(df, feature_cols=None):
    if feature_cols is None:
        # automatically select numeric features except target columns
        exclude = ['Date','Ticker','Trend','next_return','next_close']
        feature_cols = [c for c in df.columns if df[c].dtype in [np.float64, np.float32, np.int64, np.int32] and c not in exclude]
    X = df[feature_cols].fillna(0)
    y = df['Trend']
    return X, y, feature_cols

def time_split_train_test(df, split_date=None):
    # If split_date provided: train < split_date, test >= split_date
    # Otherwise split by last 20% time per ticker
    if split_date:
        train = df[df[DATE_COL] < split_date].copy()
        test = df[df[DATE_COL] >= split_date].copy()
    else:
        # compute split per ticker based on date quantile
        frames = []
        train_frames = []
        test_frames = []
        for t, g in df.groupby('Ticker'):
            g = g.sort_values(DATE_COL)
            n = len(g)
            split_idx = int(n * 0.8)
            train_frames.append(g.iloc[:split_idx])
            test_frames.append(g.iloc[split_idx:])
        train = pd.concat(train_frames)
        test = pd.concat(test_frames)
    return train, test

def train_model(X_train, y_train):
    # simple RandomForest with GridSearchCV over n_estimators
    rf = RandomForestClassifier(random_state=42, n_jobs=-1)
    param_grid = {'n_estimators':[100,200], 'max_depth':[6,10,None]}
    tscv = TimeSeriesSplit(n_splits=5)
    grid = GridSearchCV(rf, param_grid, cv=tscv, scoring='f1_macro', n_jobs=-1, verbose=1)
    grid.fit(X_train, y_train)
    print("Best params:", grid.best_params_, "Best score:", grid.best_score_)
    return grid.best_estimator_

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    print("Classification Report:\n", classification_report(y_test, y_pred))
    cm = confusion_matrix(y_test, y_pred, labels=['Up','Neutral','Down'])
    sns.heatmap(cm, annot=True, fmt='d', xticklabels=['Up','Neutral','Down'], yticklabels=['Up','Neutral','Down'])
    plt.ylabel('True')
    plt.xlabel('Predicted')
    plt.title('Confusion Matrix')
    plt.show()

def main():
    df = load_and_concat(CSV_FILES)
    print("Loaded data shape:", df.shape)
    df = basic_features(df)
    df = create_target(df)
    df = preprocess(df)
    # optional sample
    if SAMPLE:
        df = df.groupby('Ticker').tail(500)  # last 500 days per ticker (for testing)
    # choose feature columns
    X, y, feature_cols = prepare_X_y(df)
    print("Features used:", feature_cols)
    # split by time: use TEST_YEAR param if available
    if TEST_YEAR:
        split_date = pd.Timestamp(f"{TEST_YEAR}-01-01")
    else:
        split_date = None
    train_df, test_df = time_split_train_test(pd.concat([X, y, df[[DATE_COL,'Ticker']]], axis=1), split_date=split_date)
    X_train = train_df[feature_cols]
    y_train = train_df['Trend']
    X_test = test_df[feature_cols]
    y_test = test_df['Trend']
    print("Train shape:", X_train.shape, "Test shape:", X_test.shape)
    # train
    model = train_model(X_train, y_train)
    # evaluate
    evaluate_model(model, X_test, y_test)
    # save model and features
    joblib.dump({'model': model, 'features': feature_cols}, MODEL_OUT)
    print("Saved model to", MODEL_OUT)
    # Example: predict next-day trend for the latest row per ticker
    latest = df.groupby('Ticker').apply(lambda g: g.sort_values(DATE_COL).iloc[-1]).reset_index(drop=True)
    X_latest = latest[feature_cols].fillna(0)
    preds = model.predict(X_latest)
    latest_out = latest[[DATE_COL,'Ticker','Close']].copy()
    latest_out['Predicted_Trend'] = preds
    print("Predictions for latest dates:\n", latest_out)
    # show feature importance
    try:
        importances = model.feature_importances_
        fi = pd.Series(importances, index=feature_cols).sort_values(ascending=False).head(20)
        plt.figure(figsize=(8,6))
        sns.barplot(x=fi.values, y=fi.index)
        plt.title("Top feature importances")
        plt.show()
    except Exception as e:
        print("Could not display feature importances:", e)

if __name__ == "__main__":
    main()
