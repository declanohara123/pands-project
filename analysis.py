## assignment

# to investigate the Fisher's iris data set.
# investigate the data, come to conclusions based on data
# print images of data
# data set of 150 pieces of info
# sepal lenght, sepal width, petal lenght, petal width, all measureed in cm
# three different species
# iris setosa, iris versicolour, iris virginica

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import seaborn as sns

iris_data = pd.read_csv('iris.csv')

iris_data.columns = ["Sepal Lenght", "Sepal Width", "Petal Lenght", "Petal Width", "Species"]

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

#plt.show()
#plt.savefig('Histogram of....png')



## scatterplot of each pair of variables segregated by species into different colours
# x is x axis data, y is y axis data, hue allows us to differentiate based on the 'species'
# data is taken from original file iris_data
# height and aspect altered from 5 and 1 respectively to alter the image output
# the plt.suptitle adds the title to the graph
# manger = plt.get_current figure, manager.window.showMaximised() makes the new figure pop up in full screen mode
# ref for this is https://stackoverflow.com/questions/32428193/saving-matplotlib-graphs-to-image-as-full-screen
# ref for figuring the graphs https://seaborn.pydata.org/generated/seaborn.catplot.html
# set style 'ticks' makes the images easier to read by increasing the contrast of the points

sns.set_style('ticks')

sns.catplot(x='Petal Lenght',y='Petal Width',hue='Species', data=iris_data, height=7, aspect=1.25)
plt.suptitle('Petal Lenght versus Petal Width')
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.show()

sns.catplot(x='Petal Lenght',y='Sepal Width',hue='Species', data=iris_data, height=7, aspect=1.25)
plt.suptitle('Petal Lenght versus Sepal Width')
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.show()

sns.catplot(x='Petal Lenght',y='Sepal Lenght',hue='Species', data=iris_data, height=7, aspect=1.25)
plt.suptitle('Petal Lenght versus Sepal Lenght')
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.show()

sns.catplot(x='Petal Width',y='Sepal Width',hue='Species', data=iris_data, height=7, aspect=1.25)
plt.suptitle('Petal Width versus Sepal Width')
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.show()

sns.catplot(x='Petal Width',y='Sepal Lenght',hue='Species', data=iris_data, height=7, aspect=1.25)
plt.suptitle('Petal Width versus Sepal Lenght')
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.show()

sns.catplot(x='Sepal Lenght',y='Sepal Width',hue='Species', data=iris_data, height=7, aspect=1.25)
plt.suptitle('Sepal Lenght versus Sepal Width')
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.show()