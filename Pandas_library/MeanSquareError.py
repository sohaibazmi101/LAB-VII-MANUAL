import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder

temp = np.array([10,15,20,25,30,12,18,23,28,32]).reshape(-1,1)
kwh = np.array([50, 60, 75, 90, 105, 55, 70, 85, 95, 110])
x_train, x_test, y_train, y_test = train_test_split(temp, kwh, test_size=0.3, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
mse = mean_squared_error(y_pred, y_test)
print("Mean Square Error: ", mse)
print("Predicted Value: ", y_pred)
print("Actual Value: ", np.array(y_test))

plt.scatter(x_train, y_train)
plt.plot(x_train, y_pred)
plt.xlabel("Temperature")
plt.ylabel("KWH")
plt.show()