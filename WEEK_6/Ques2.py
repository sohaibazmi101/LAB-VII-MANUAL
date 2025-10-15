from sklearn.datasets import load_iris
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Load dataset
iris = load_iris(as_frame=True)
iris_df = iris.frame

print("Iris Data (first 5 rows):\n", iris_df.head())
print("\nColumns:\n", iris_df.columns)

# Select numeric features correctly
numeric_features = ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"]
iris_features_df = iris_df[numeric_features]

# Normalize (Min-Max Scaling)
scaler_minmax = MinMaxScaler()
normalized_array = scaler_minmax.fit_transform(iris_features_df)
normalized_df = pd.DataFrame(normalized_array, columns=numeric_features)
print("\nNormalized Features (Min-Max Scaling, first 5 rows):\n", normalized_df.head())

# Apply Standardization (Z-score Scaling)
scaler_standard = StandardScaler()
standardized_array = scaler_standard.fit_transform(iris_features_df)
standardized_df = pd.DataFrame(standardized_array, columns=numeric_features)
print("\nStandardized Features (Z-score Scaling, first 5 rows):\n", standardized_df.head())
