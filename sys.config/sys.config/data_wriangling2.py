import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("academic_performance.csv")
df.head()

print("Missing values per columns: ")
print(df.isnull().sum())

df['Sub1'] = df['Sub1'].fillna(df['Sub1'].mean()).round(2)
df['Sub2'] = df['Sub2'].fillna(df['Sub2'].mean()).round(2)
df['Sub3'] = df['Sub3'].fillna(df['Sub3'].mean()).round(2)
df['Attendance'] = df['Attendance'].fillna(df['Attendance'].mean()).round(2)

df.head()

sns.boxplot(data=df[['Sub1','Sub2','Sub3']])
plt.title("Boxplot of Subject Marks")
plt.show()

def inter_quartile_range(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5*IQR
    upper = Q3 + 1.5*IQR
    outliers = data[(data[column] < lower) | (data[column] > upper)]
    print("lower bound", lower)
    print("upper bound", upper)
    print("IQR", IQR)

    flagged = outliers[['StudentID', column]]
    print(f"flagged outliers for {column}")
    print(flagged)

    cleaned_data = data[(data[column] >= lower) & (data[column] <= upper)]
    return cleaned_data


df_cleaned = inter_quartile_range(df, 'Sub1')
df_cleaned = inter_quartile_range(df, 'Sub2')
df_cleaned = inter_quartile_range(df, 'Sub3')
df_cleaned.head()


sns.boxplot(data=df_cleaned[['Sub1', 'Sub2', 'Sub3']])
plt.title("Boxplot for performance")
plt.show()

df_cleaned['Attendance'].hist()
plt.title("Before Transformation")
plt.show()

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

df_cleaned.loc[:, 'Attendance_scaled'] = scaler.fit_transform(df_cleaned[['Attendance']])
print(df_cleaned[['Attendance', 'Attendance_scaled']])

df_cleaned['Attendance_scaled'].hist()
plt.title("After Transformation")
plt.show()