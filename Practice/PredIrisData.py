import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris = load_iris(as_frame=True)
x = iris.data
y = iris.target
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.9, random_state=42)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train, y_train)
y_pred= knn.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Prediction on X train: \n{y_pred}")
print(f"Actual Value: \n{y_test}")
print(f"Accuracy Score:\n{round(accuracy, 2)}")