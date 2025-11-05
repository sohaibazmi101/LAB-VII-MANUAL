import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np

fruit_data = {
    "Color": [1, 2, 3, 3, 4, 4, 1, 2, 3, 4],
    "Size": [7.0, 6.5, 8.0, 7.5, 6.0, 6.8, 7.2, 6.3, 7.8, 6.5],
    "Fruit": ["Apple", "Apple", "Banana", "Banana", "Orange", "Orange", "Apple", "Apple", "Banana", "Orange"]
}

df = pd.DataFrame(fruit_data)

x = df[['Color', 'Size']]
y = df['Fruit']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3, random_state=42)
print(x_train.head())
print(y_train.head())

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train, y_train)
pred = knn.predict(x_test)
accuracy = accuracy_score(pred, y_test)
print(accuracy)
print("Actual: ", np.array(y_test))
print("predicted: ", pred)