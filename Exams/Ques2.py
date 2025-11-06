import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data1 = {
    'size': [1.2, 1.1, 1.0, 6.0, 6.4, 6.3, 11.4, 12.0, 11.9, 11.6],
    'color': [101, 102, 100, 600, 604, 603, 1100, 1200, 1190, 1160],
    'fruit': ['Apple', 'Apple', 'Apple', 'Banana', 'Banana', 'Banana', 'WaterMelon', 'WaterMelon', 'WaterMelon', 'WaterMelon']
}



df = pd.DataFrame(data1)

x = df[['size', 'color']]
y = df['fruit']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
model = KNeighborsClassifier(n_neighbors=3)
model.fit(x_train, y_train)
pred = model.predict(x_test)
accuracy = accuracy_score(pred, y_test)
scale = StandardScaler()
scale_data = scale.fit_transform(x)
x_df = pd.DataFrame(scale_data, columns=x.columns)
x_df_train, x_df_test, y_df_train, y_df_test = train_test_split(x_df, y, test_size=0.3, random_state=42)
model.fit(x_df_train, y_df_train)
prediction = model.predict(x_df_test)
accuracy_df = accuracy_score(prediction, y_df_test)
print("Accuracy First: ", accuracy)
print("Accuracy Second: ", accuracy_df)