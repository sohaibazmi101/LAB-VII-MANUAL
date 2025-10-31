import pandas as pd
from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing(as_frame=True)
housing_df = housing.frame
print(housing_df.head())
print(f'Colums: {housing_df.columns}')
print(f"Null Values: \n", housing_df.isnull().sum())
print(f"Summary: \n{housing_df.describe()}")
print("Correlation: ", housing_df.corr()['HouseAge'])