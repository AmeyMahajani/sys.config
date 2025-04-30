import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Iris.csv")
df.head()

df.info()

plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
sns.histplot(df['sepal_length'], bins=30, kde=True)

plt.subplot(2,2,2)
sns.histplot(df['sepal_width'], bins=30, kde=True)

plt.subplot(2,2,3)
sns.histplot(df['petal_length'], bins=30, kde=True)

plt.subplot(2,2,4)
sns.histplot(df['petal_width'], bins=30, kde=True)


plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
sns.boxplot(x='species', y='sepal_length', data=df)

plt.subplot(2,2,2)
sns.boxplot(x='species', y='sepal_width', data=df)

plt.subplot(2,2,3)
sns.boxplot(x='species', y='petal_length', data=df)

plt.subplot(2,2,4)
sns.boxplot(x='species', y='petal_width', data=df)
