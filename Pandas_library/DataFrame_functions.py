import pandas as pd

# What is a DataFrame?
# DataFrame is a two dimenstional Data structure, like 2-D array or a table with rows and columns.

# How to create it

data = {
    "col1": [1,2,3,4,5],
    "col2": [4,5,6,7,8]
}

df = pd.DataFrame(data)
print(df)

# Locate Rows
#  It uses loc attribute to show one or more rows in a DataFrame

print(df.loc[[1,3]])

data1 = {
    'calories': [10,20,30,25],
    'duration': [1,2,3,2.5]
}
df1 = pd.DataFrame(data1, index=['Day1', 'Day2', 'Day3', 'Day4'])
print(df1)
print(df1.loc['Day3'])