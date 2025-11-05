import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
data = {
    'Age': np.random.randint(20,60,100),
    'PurchaseFrequency': np.random.uniform(0.5, 5, 100).round(1),
    'RespondToCompaign': np.random.choice([0,1], 100, p=[0.6, 0.4])
}

for i in range(100):
    if data['Age'][i] < 35 and data['PurchaseFrequency'][i] > 3:
        data['RespondToCompaign'][i] = 1
    elif data['Age'][i] > 50 and data['PurchaseFrequency'][i] < 1.5:
        data['RespondToCompaign'][i] = 0

df = pd.DataFrame(data)
x = df[['Age', 'PurchaseFrequency']]
y = df['RespondToCompaign']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
print(x_train)
print(y_train)