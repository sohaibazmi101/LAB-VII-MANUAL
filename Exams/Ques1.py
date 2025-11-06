import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.metrics import accuracy_score

data = np.array([[1,2,3,4,5],
                 [10,11,12,13,14],
                 [20,21,22,23,24],
                 [25,26,27,28,29]])

cols = ['col1', 'col2', 'col3', 'col4', 'col5']
df = pd.DataFrame(data, columns=cols)
min_max = MinMaxScaler()
df_min_max = min_max.fit_transform(df)
standar_scaler =StandardScaler()
df_stand = standar_scaler.fit_transform(df)
print('Original Array: \n', df)
print("Min Max Scaled: \n", pd.DataFrame(df_min_max, columns=cols))

print("Standard Scaler: \n", pd.DataFrame(df_stand, columns=cols))

print("Means : Col1: ", df['col1'].mean())
print("Means : Col2: ", df['col2'].mean())
print("Means : Col3: ", df['col3'].mean())
print("Means : Col4: ", df['col4'].mean())
print("Means : Col5: ", df['col5'].mean())