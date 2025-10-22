import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = {
    'Age': np.random.randint(20, 60, 100),
    'PurchaseFrequency': np.random.uniform(0.5, 5, 100).round(1),
    'RespondedToCampaign': np.random.choice([0, 1], 100, p=[0.6, 0.4])
}
for i in range(100):
    if data['Age'][i] < 35 and data['PurchaseFrequency'][i] > 3:
        data['RespondedToCampaign'][i] = 1
    elif data['Age'][i] > 50 and data['PurchaseFrequency'][i] < 1.5:
        data['RespondedToCampaign'][i] = 0
df = pd.DataFrame(data)
X = df[['Age', 'PurchaseFrequency']]
y = df['RespondedToCampaign']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
print("Campaign Response Data (X_train head):\n", X_train.head())
print("\nCampaign Response Target (y_train head):\n", y_train.head())
dtree = DecisionTreeClassifier(max_depth=3, random_state=42)
dtree.fit(X_train, y_train)
y_pred = dtree.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("\nPredictions on X_test:\n", y_pred)
print("\nActual responses:\n", list(y_test))
print("\nDecision Tree Accuracy:", round(accuracy, 2))