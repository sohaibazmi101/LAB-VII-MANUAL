import pandas as pd

# df = pd.read_csv('data.csv')
# print(df.head())
# df.dropna(inplace=True)

# x = df['Calories'].mean()
# print(x)
# df.fillna({'Calories' : x}, inplace=True)
# print(df.to_string())
# print(x)

# df = pd.DataFrame({'date': ['2022-12-01', '01/02/2022', '2022-03-23', '03/02/2022', '3 4 2023', '2023.9.30']})
# print(df)
# df['date'] = pd.to_datetime(df['date'], format='mixed', dayfirst=True)

# print(df)
import pandas as pd

# create dataframe
data = {
    'Country': ['USA', 'Canada', 'Australia', 'Germany', 'Japan'],
    'Date': ['2023-07-20', '2023-07-21', '2023-07-22', '2023-07-23', '2023-07-24'],
    'Temperature': [25.5, '28.0', 30.2, 22.8, 26.3]
}
df = pd.DataFrame(data)

df['Temperature'] = df['Temperature'].astype(float)
print(df)
mean = df['Temperature'].mean()
print(mean)