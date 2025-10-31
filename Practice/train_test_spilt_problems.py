import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

data = pd.DataFrame({
    'Age': [23,19,18,21,24,26,25,23,21,22,28,19],
    'Marks': [91,56,45,76,89,79,90,45,67,43,67,93]
})
train_df, test_df = train_test_split(data, test_size=0.20, random_state=42)
print("Train DF: \n", train_df)
print('Test DF:\n', test_df)
print('Size: ', len(train_df))

X = np.random.randint(1,100, (10,3))
y = np.array(['A','B', 'A', 'C', 'B', 'A','A','C','A','B'])
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=1)
print("X train: \n", X_train)
print('X test: \n', X_test)
print("Y train: ", y_train)
print("Y test: ", y_test)

# Problem 3 Advanced

datas = {
    'Feature1': range(1,11),
    'Feature2': range(11,21),
    'Label': ['A','A','A','B','B', 'C','C','C', 'C','C']
}
df = pd.DataFrame(datas)
train_df, test_df = train_test_split(df, test_size=0.25, random_state=34, stratify=df['Label'])
print('Train df Lable Count: \n', train_df['Label'].value_counts())
print("Test Df Label Count: \n", test_df['Label'].value_counts())