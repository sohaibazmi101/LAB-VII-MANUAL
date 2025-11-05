import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

data = {
 'Size_cm': [7, 7.5, 6.8, 18, 19, 17.5, 8.5, 9, 8.2, 7.2],
 'Color_Intensity': [0.8, 0.75, 0.82, 0.6, 0.58, 0.62, 0.9, 0.88, 0.92, 0.78],
 'FruitType': ['Apple', 'Apple', 'Apple', 'Banana', 'Banana', 'Banana', 'Orange', 'Orange', 'Orange', 'Apple']
}

df = pd.DataFrame(data)
X = df[["Size_cm", "Color_Intensity"]]
y = df["FruitType"]

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print(x_train)
print(y_train)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train, y_train)
predict = knn.predict(x_test)
accuracy = accuracy_score(y_test, predict)
print("Accuracy: ",accuracy)
print(f"Predicted : {predict} : Original : {y_test}")