import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")
df.head()

plt.figure(figsize=(10,6))
sns.boxplot(x='sex', y='age', data=df, hue='survived')
sns.swarmplot(x='sex', y='age', hue='survived', data=df, dodge=True, size=3, palette='dark:green')
plt.title('Distribution of Age with respect to Gender and Survival Status')

sns.swarmplot(x='sex', y='age', hue='survived', data=df, dodge=True, size=3)
