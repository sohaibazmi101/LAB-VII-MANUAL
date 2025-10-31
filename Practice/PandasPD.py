import pandas as pd
df = pd.DataFrame({
    'Name': ['Ali', 'Azmi', 'Syed', 'Abid'],
    'Marks': [90, 71, 39, 91],
    'Age': [24, 22, 23, 19]
})
print(df)
print("Average: ", df['Marks'].mean())
print("Oldest Student: ", df.loc[df['Age'].idxmax(), 'Name'])
print(df[df['Marks']>80])
df['grade'] = df['Marks'].apply(lambda x: 'A' if x > 90 else ('B' if x > 80 else 'C'))
print(df)