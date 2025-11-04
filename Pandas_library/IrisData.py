import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler, StandardScaler

iris = load_iris(as_frame=True)
iris_df = iris.frame
# print(iris_df.head())

numerical_features = iris_df[['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']]

# print(numerical_features.head())

min_max = MinMaxScaler()

normalized = min_max.fit_transform(numerical_features)
normalized_df = pd.DataFrame(normalized, columns=['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'])
print(normalized_df.head())

standard = StandardScaler()

standardized = standard.fit_transform(numerical_features)
standardized_df = pd.DataFrame(standardized, columns=['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'])
print(standardized_df.head())
print(standardized_df.max())