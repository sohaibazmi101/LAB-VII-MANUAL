import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

temp = np.array([10, 15, 20, 25, 30, 12, 18, 23, 28, 32]).reshape(-1, 1)
kwh = np.array([50, 60, 75, 90, 105, 55, 70, 85, 95, 110])
X_train_elec, X_test_elec, y_train_elec, y_test_elec = train_test_split(
    temp, kwh, test_size=0.3, random_state=42
)
print("\nElectricity Consumption Data (X_train_elec):\n", X_train_elec[:5])
print("\nElectricity Consumption (y_train_elec):\n", y_train_elec[:5])
lin_reg = LinearRegression()
lin_reg.fit(X_train_elec, y_train_elec)
y_pred_elec = lin_reg.predict(X_test_elec)
mse = mean_squared_error(y_test_elec, y_pred_elec)
print("\nPredictions on X_test_elec:\n", y_pred_elec)
print("\nActual Electricity Consumption:\n", y_test_elec)
print("\nMean Squared Error (MSE):", round(mse, 2))
plt.scatter(X_train_elec, y_train_elec, color='blue', label='Training Data')
plt.plot(X_train_elec, lin_reg.predict(X_train_elec), color='red', linewidth=2, label='Regression Line')
plt.xlabel('Temperature (°C)')
plt.ylabel('Electricity Consumption (kWh)')
plt.title('Linear Regression: Temperature vs Electricity Consumption')
plt.legend()
plt.grid(True)
plt.show()