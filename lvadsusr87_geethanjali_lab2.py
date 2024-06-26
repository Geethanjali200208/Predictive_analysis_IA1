# -*- coding: utf-8 -*-
"""LVADSUSR87-geethanjali-Lab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TsUZ8plolDA9GKBR93i0mmtH7kN0Tmo3
"""

#classification
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("/content/booking.csv")
print(data.info())
# 1 handling missing values and outliers
data = data.dropna()
data = data.drop_duplicates()
Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3 - Q1
outliers = ((data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))).any(axis=1)
print("Number of outliers detected:", outliers.sum())
# Pairplot for numerical variables without outliers
sns.pairplot(data[~outliers])
plt.show()
#2 Features and labels
X = data.drop(columns=['Booking_ID', 'booking status'])
y = data['booking status']

#3 Encoding categorical variables
label_encoder = LabelEncoder()
X_encoded = X.apply(label_encoder.fit_transform)
#4 Data splitting
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)
#5 model development and training data
clf = LogisticRegression()
clf.fit(X_train, y_train)
predicted_cancelled = clf.predict(X_test)
#6 model evaluation
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label='Canceled')
recall = recall_score(y_test, y_pred, pos_label='Canceled')
f1 = f1_score(y_test, y_pred, pos_label='Canceled')
conf_matrix = confusion_matrix(y_test, y_pred)
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)
print("Confusion Matrix:")
print(conf_matrix)