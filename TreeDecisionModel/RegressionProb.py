import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

temp = np.array([10,15,20,25,30,12,18,23,28,32]).reshape(-1,1)
kwh = np.array([50, 60, 75, 90, 105, 55, 70, 85, 95, 110])

x_train, x_test, y_train, y_test = train_test_split(temp, kwh, test_size=0.3, random_state=42)

model = DecisionTreeRegressor(max_depth=3)
model.fit(x_train, y_train)
pred = model.predict(x_test)
mse = mean_squared_error(pred, y_test)
print("MSE : ", mse)
print("Actual Data: ", np.array(y_test))
print("Predic")