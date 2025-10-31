import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = {
    'Size_cm': [7.0, 7.5, 6.8, 18.0, 19.0, 17.5, 8.5, 9.0, 8.2, 7.2],
    'Color_Intensity': [0.82, 0.80, 0.78, 0.60, 0.58, 0.62, 0.90, 0.88, 0.92, 0.79],
    'FruitType': ['Apple', 'Apple', 'Apple', 'Banana', 'Banana', 'Banana', 'Orange', 'Orange', 'Orange', 'Apple']
}

df = pd.DataFrame(data)

x = df[['Size_cm', 'Color_Intensity']]
y = df['FruitType']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=42)
print(f"X train: \n{x_train}")
print(f"Y train: \n{y_train}")
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Prediction on x test:\n{y_pred}")
print(f"Actual fruit type: \n{y_test}")
print(f"Accuracy Score: {round(accuracy, 2)}")