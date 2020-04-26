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
import matplotlib.pyplot as plt
import csv
import seaborn as sns

iris_data = pd.read_csv('iris.csv')

iris_data.columns = ["sepal lenght", "sepal width", "petal lenght", "petal width", "species"]


#summary = iris_data.describe()
#summary = summary.transpose()
#print(summary.head())

#summary of sepal lenght = open("summary of iris data.txt", "w")
#file.print(iris_data["sepal lenght"].describe())
  #  file.close

#print(iris_data["sepal lenght"].describe())
#print(iris_data["sepal width"].describe())
#print(iris_data["petal lenght"].describe())
#print(iris_data["petal width"].describe())

#sns.pairplot(iris_data,  hue="species", kind="scatter")

#plt.show()

#plt.close()
#f = open("Sepal Lenght Summary.txt", "a")
#f.write(print(iris_data["sepal lenght"].describe()))
#f.close()

#stdout = open("test.txt", "w")
#print(iris_data["sepal lenght"].describe())
#stdout. close()

#with open("iris.csv") as f:
 #   with open("sepal lenght.txt", "w") as f1:
  #      for line in f:
   #         f1.write("iris data")


#g = print(iris_data["sepal lenght"].describe())

#f = open("Sepal Lenght Summary.txt", "a")
#f.write("g")
#f.close()

#plt.scatter(iris_data['sepal lenght'], iris_data['sepal width'])
#plt.title('Sepal Lenght versus Sepal Width')
#plt.show()

#plt.scatter(iris_data['sepal lenght'], iris_data['petal lenght'])
#plt.title('Sepal lenght versus Petal lenght')
#plt.show()

#plt.scatter(iris_data['sepal lenght'], iris_data['petal width'])
#plt.title('sepal lenght versus petal width')
#plt.show()

#plt.scatter(iris_data['sepal width'], iris_data['petal width'])
#plt.title('sepal width versus width width')
#plt.show()

#iris_data.hist(column='petal lenght', by='species', bins=40)

#plt.show()

sns.pairplot(iris_data, hue='species', vars=['sepal width', 'sepal lenght'], diag_kind="kde")
plt.show()