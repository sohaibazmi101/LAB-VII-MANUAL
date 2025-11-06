import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

np.random.seed(42)
data = {
    'keywords': np.random.randint(0,10,100)
}
df = pd.DataFrame(data)
y = np.random.randint(5,10,100)
for i in range(100):
    if df['keywords'][i] <=5:
        y[i] = 0
    elif df['keywords'][i] < 8:
        y[i] = 1

x = df[['keywords']]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
model = LogisticRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_pred, y_test)
print("Accuracy: ", accuracy)
print("Actual Data: ", np.array(y_test))
print("Predicted Data: ", y_pred)
