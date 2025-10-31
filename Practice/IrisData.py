import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler, StandardScaler

iris = load_iris(as_frame=True)
iris_df = iris.frame
print(iris_df.head())
numeric_feature = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
iris_feature = iris_df[numeric_feature]
iris_feature_df = pd.DataFrame(iris_feature, columns=numeric_feature)
minmax_scaler = MinMaxScaler()
normalized = minmax_scaler.fit_transform(iris_feature_df)
normalized_df = pd.DataFrame(normalized, columns=numeric_feature)
print(normalized_df.head())
standard_scaler = StandardScaler()
standard = standard_scaler.fit_transform(iris_feature_df)
standard_df = pd.DataFrame(standard, columns=numeric_feature)
print(standard_df.head())