import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")
df.head()

sns.countplot(x='sex', hue='survived', data=df)
plt.title("Survival based on sex")
plt.show()

sns.countplot(x='pclass', hue='survived', data=df)
plt.title("Survival based on passenger class")
plt.show()

sns.histplot(df['age'], kde=True)

df['survival'] = df['survived'].map({0:'No', 1:'Yes'})

sns.countplot(x='survival', data=df)
plt.title("Survival")
plt.show()

sns.scatterplot(x='age', y='fare', data=df, hue='survival')
plt.title("Survival based on age and fare")
plt.show()

import numpy as np

corr = df.corr(numeric_only=True)

plt.figure(figsize=(10,8))
sns.heatmap(corr, annot=True, cmap='Blues')
plt.title("Correlation Heatmap")

sns.histplot(df['fare'], kde=True, bins=20)
plt.title('Distribution of Fare Prices')
plt.xlabel('Fare')
plt.ylabel('Number of Passengers')