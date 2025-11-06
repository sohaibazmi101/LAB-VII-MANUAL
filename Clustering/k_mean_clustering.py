import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

small_animals = np.random.normal(loc=[5, 20], scale=[1, 5], size=(20, 2))
medium_animals = np.random.normal(loc=[50, 80], scale=[10, 15], size=(20, 2))
large_animals = np.random.normal(loc=[300, 150], scale=[50, 25], size=(20, 2))

df = pd.DataFrame(np.vstack([small_animals, medium_animals, large_animals]), columns=['Weight_kg', 'Height_cm'])

scaler = StandardScaler()
scaled = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled, columns=df.columns)

model = KMeans(n_clusters=3, random_state=42)
model.fit(scaled_df)
clusters = model.labels_
df['Cluster'] = clusters
print(df.to_string())