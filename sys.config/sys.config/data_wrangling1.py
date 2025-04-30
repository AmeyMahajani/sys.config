import numpy as np
import pandas as pd
df = pd.read_csv("iris.csv")
df.head()

df.isnull().sum()

print("Initial Statistics: ")
df.describe()

df.info()

df.shape

df.dtypes

df['species'] = df['species'].astype('category')
df.dtypes

columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder

scaler = MinMaxScaler()
df[columns] = scaler.fit_transform(df[columns])
print("\nNormalized Data (first 5 rows using MinMaxScaler):")
df.head()

scaler = StandardScaler()
df[columns] = scaler.fit_transform(df[columns])
print("Standardized data using sklearn")
df.head()

label_encoder = LabelEncoder()
df['Species'] = label_encoder.fit_transform(df['species'])
df.tail()

df.info()

print("species encoding")
for i, species in enumerate(label_encoder.classes_):
    print(f"{species} : {i}")