import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, precision_score, f1_score

df = pd.read_csv("/content/Iris.csv")
df.head()

df.shape

df.describe()

df.info()

x = df.drop(columns=['Species'])
y = df['Species']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=42)

from sklearn.naive_bayes import GaussianNB

model = GaussianNB()

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

cm = confusion_matrix(y_test, y_pred)
cm

accuracy = accuracy_score(y_test, y_pred)
accuracy

error_rate = 1-accuracy
error_rate

precision = precision_score(y_test, y_pred, average='weighted')
precision

recall = recall_score(y_test, y_pred, average='weighted')
recall

f1 = f1_score(y_test, y_pred, average='weighted')
f1

sns.heatmap(cm, annot=True, fmt='d', cmap='Greys')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title("Confusion Matrix")