import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

X_shapes = np.array([
[4, 1.0], [4, 1.05], [4, 0.95],
[0, 1.0], [0, 1.1], [0, 0.9],
[4, 0.5], [0, 2.0]
])
y_shapes = np.array([0,0,0,1,1,1,0,1])

x_train, x_test, y_train, y_test = train_test_split(X_shapes, y_shapes, test_size=0.3, random_state=42)
model = MLPClassifier(hidden_layer_sizes=(5,), max_iter=5000, random_state=42, solver='adam')
model.fit(x_train, y_train)
predict = model.predict(x_test)
accuracy = accuracy_score(predict, y_test)
print("Predicted: ",accuracy)
print("Actual Data: ", np.array(y_test))
print("Predicted Data: ", predict)