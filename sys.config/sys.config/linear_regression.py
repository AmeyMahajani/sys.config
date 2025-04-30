import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("/content/BostonHousing.csv")
df.head()

df.info()

df.describe()

df.shape

df.isnull().sum()

df_cleaned = df.dropna()
df_cleaned.head()

df_cleaned.isnull().sum()

df.columns

x=df_cleaned.drop('medv', axis=1)
y=df_cleaned['medv']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

model = LinearRegression()

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

mse = mean_squared_error(y_test, y_pred)
mse

r2=r2_score(y_test, y_pred)
r2

plt.scatter(y_test, y_pred, color='blue')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linewidth=2)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual vs Predicted Prices')

comparison_df=pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
comparison_df.head()