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

# file=open creates a new file in the current directory named whatever is in "" after the bracket
# the .txt after the standard names makes the new file a text file
# "w" is the write function which allows us to populate the file with data
# file.write is the command to write the follwing sequence
# due to describe being an output and not a string it has to be given the f function and put in curly brackets
# this allows python to determine the output and add it to the rest of the sentence I've typed as a string

#file=open("Summary of Sepal Lenght.txt", "w")
#file.write(f'The summary of Sepal Lenght is {iris_data["sepal lenght"].describe()}\n')

#file=open("Summary of Sepal Width.txt", "w")
#file.write(f'The summary of Sepal Width is {iris_data["sepal width"].describe()}\n')

#file=open("Summary of Petal Lenght.txt", "w")
#file.write(f'The summary of Petal Lenght is {iris_data["petal lenght"].describe()}\n')

#file=open("Summary of Petal Width.txt", "w")
#file.write(f'The summary of Petal Width is {iris_data["petal width"].describe()}\n')



#save a histogram of each variable to a .png file





# scatterplot of each pair of variables segregated by species into different colours
# x is x axis data, y is y axis data, hue allowsus to differentiate based on the 'species'
# data is taken from original file
# ref for figuring this out https://towardsdatascience.com/data-visualization-using-seaborn-fc24db95a850



sns.catplot(x='petal lenght',y='petal width',hue='species', data=iris_data, )
plt.show()

sns.catplot(x='petal lenght',y='sepal width',hue='species', data=iris_data)
plt.show()

sns.catplot(x='petal lenght',y='sepal lenght',hue='species', data=iris_data)
plt.show()

sns.catplot(x='petal width',y='sepal lenght',hue='species', data=iris_data)
plt.show()

sns.catplot(x='petal width',y='sepal width',hue='species', data=iris_data)
plt.show()

sns.catplot(x='sepal lenght',y='sepal width',hue='species', data=iris_data)
plt.show()

