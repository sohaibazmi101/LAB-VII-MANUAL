import pandas as pd

# to read a CSV file we use function know as read_csv()

df = pd.read_csv('data.csv')
print(df.to_string())
print(pd.options.display.max_rows)
print(df.info())
df = pd.DataFrame(df)
print("X--------x")
x = df.head(10)
print(x)