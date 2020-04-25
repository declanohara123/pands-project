## assignment
#
# to investigate the Fisher's iris data set.
# investigate the data
# come to conclusions based on data
# print images of data
#
# data set of 150 pieces of info
# 
# sepal lenght
# sepal width
# petal lenght
# petal width
# all measureed in cm

# three different species
# iris setosa
# iris versicolour
# iris virginica

import numpy as np
import pandas as pd
import matplotlib as plt
import csv
import seaborn as sns

iris_data = pd.read_csv('iris.csv')

iris_data.columns = ["sepal lenght", "sepal width", "petal lenght", "petal width", "species"]


summary = iris_data.describe()
summary = summary.transpose()
print(summary.head())

print(iris_data["sepal lenght"].describe())
print(iris_data["sepal width"].describe())
print(iris_data["petal lenght"].describe())
print(iris_data["petal width"].describe())
