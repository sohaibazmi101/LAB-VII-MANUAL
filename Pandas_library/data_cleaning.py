import pandas as pd
import matplotlib.pyplot as plt

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
# data = {
#     'Country': ['USA', 'Canada', 'Australia', 'Germany', 'Japan'],
#     'Date': ['2023-07-20', '2023-07-21', '2023-07-22', '2023-07-23', '2023-07-24'],
#     'Temperature': [25.5, '28.0', 30.2, 22.8, 26.3]
# }
# df = pd.DataFrame(data)

# df['Temperature'] = df['Temperature'].astype(float)
# print(df)
# mean = df['Temperature'].mean()
# print(mean)

# df = pd.DataFrame({'Temp': [10,11,21,12,11,13,14,19,33,120]})
# print(df)
# df.loc[2, 'Temp'] = 19
# print(df)
# for x in df.index:
#     if df.loc[x, 'Temp'] > 20:
#         df.loc[x, 'Temp'] = 19
# print(df)

data = pd.read_csv('data.csv')
print(data.info(['Pulse']))
# print(data.corr())
# data.plot()
# plt.show()