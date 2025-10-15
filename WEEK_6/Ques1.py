from sklearn.datasets import fetch_california_housing
import pandas as pd
housing = fetch_california_housing(as_frame=True)
housing_df = housing.frame
print("California housing data (first 5 rows):\n", housing_df.head())
print("\nOriginal columns:\n", housing_df.columns)