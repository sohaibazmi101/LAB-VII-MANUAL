import pandas as pd

# to read a CSV file we use function know as read_csv()

df = pd.read_csv('data.csv')
pd.options.display.max_rows = 9999
print(df.to_string())
print(pd.options.display.max_rows)
print(df.info())