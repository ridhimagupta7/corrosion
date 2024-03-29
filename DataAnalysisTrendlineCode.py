# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wxecqPk5Oiyb3vumGNvJWmZaWrby1_TY
"""

import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data
x = np.array([956, 923, 895, 936, 961, 1016, 1068, 1092, 1140, 1176, 1208]).reshape((-1, 1))
y = np.array([0, 24, 45, 70, 120, 170, 216, 286, 335, 383, 431])

x_squared = x ** 2

X_new = np.concatenate((x_squared, x), axis=1)

model = LinearRegression()
model.fit(X_new, y)

x_new_value = np.array([[6 ** 2, 6]])  # Square the new x value and reshape to match the feature matrix shape
y_pred = model.predict(x_new_value)

print("Predicted value:", y_pred[0])
