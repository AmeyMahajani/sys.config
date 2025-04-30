import numpy as np
import pandas as pd
df = pd.read_csv("/content/Iris.csv")
df.head()

# print("\nSummary statistics grouped by species:")
# grouped_stats = iris.groupby('species').describe()
# print(grouped_stats)

numeric_cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
setosa = df[df['species'] == 'setosa'][numeric_cols]
versicolor = df[df['species'] == 'versicolor'][numeric_cols]
virginica = df[df['species'] == 'virginica'][numeric_cols]

# Statistics for Iris-setosa
print("\nStatistics for Iris-setosa:")
print(f"Count: {len(setosa)}")
print("Mean values:")
print(setosa.mean())
print("\nStandard Deviation:")
print(setosa.std())
print("\nPercentiles (25%, 50%, 75%):")
print(setosa.quantile([0.25, 0.5, 0.75]))
print("\nMinimum values:")
print(setosa.min())
print("\nMaximum values:")
print(setosa.max())

# Statistics for Iris-versicolor
print("\nStatistics for Iris-versicolor:")
print(f"Count: {len(versicolor)}")
print("Mean values:")
print(versicolor.mean())
print("\nStandard Deviation:")
print(versicolor.std())
print("\nPercentiles (25%, 50%, 75%):")
print(versicolor.quantile([0.25, 0.5, 0.75]))
print("\nMinimum values:")
print(versicolor.min())
print("\nMaximum values:")
print(versicolor.max())

# Statistics for Iris-virginica
print("\nStatistics for Iris-virginica:")
print(f"Count: {len(virginica)}")
print("Mean values:")
print(virginica.mean())
print("\nStandard Deviation:")
print(virginica.std())
print("\nPercentiles (25%, 50%, 75%):")
print(virginica.quantile([0.25, 0.5, 0.75]))
print("\nMinimum values:")
print(virginica.min())
print("\nMaximum values:")
print(virginica.max())


# Comprehensive statistics using describe()
print("\nComprehensive statistics using describe():")
print("\nIris-setosa:")
print(setosa.describe())
print("\nIris-versicolor:")
print(versicolor.describe())
print("\nIris-virginica:")
print(virginica.describe())