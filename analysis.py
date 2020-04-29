## assignment
# to investigate the Fisher's iris data set.
# investigate the data, come to conclusions based on data
# print images of data, as well as files of summarys
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

## saving  summary of each varible to a file in the current folder
# file=open creates a new file in the current directory named whatever is in "" after the bracket
# the .txt after the standard names makes the new file a text file
# "w" is the write function which allows us to populate the file with data
# file.write is the command to write the follwing sequence
# due to describe being an output and not a string it has to be given the f function and put in curly brackets
# this allows python to determine the output and add it to the rest of the sentence I've typed as a string

file=open("Table 1. Summary of Sepal Lenght.txt", "w")
file.write(f'The summary of the Sepal Lenght is {iris_data["Sepal Lenght"].describe()}\n')

file=open("Table 2. Summary of Sepal Width.txt", "w")
file.write(f'The summary of the Sepal Width is {iris_data["Sepal Width"].describe()}\n')

file=open("Table 3. Summary of Petal Lenght.txt", "w")
file.write(f'The summary of the Petal Lenght is {iris_data["Petal Lenght"].describe()}\n')

file=open("Table 4. Summary of Petal Width.txt", "w")
file.write(f'The summary of the Petal Width is {iris_data["Petal Width"].describe()}\n')


## save a Kernel density estimation of each variable to a .png file
# I tried loads of varients of catplots but I just didn't like the final results with regards histogram style
# Settled for the pairplot as it gives a nicer final image, that while strictly is a Kernel density estimation
# rather than a histogram the output image is fairly similar I just prefer the curves to the bar charts for aesthetics
# pairplot gives us the option of several or singular charts, I reduced the amount of variables using vars=[]
# in this case data is the iris_data file
# hue= seperates the data based on the species in this case
# vars= as mentioned above seperated out the variables to graph
# height changes the size out put of the image
# plt.suptitle = gives the graph a name and fontsize allters the size of given name
# pltclose() is added at the end of each graph as the next plt.show() function in part of the next section
# this kept putting up these graphs when I didn't want to so had to add it in
# set style 'ticks' makes the images easier to read by increasing the contrast of the points, allegedly

sns.set_style('ticks')

sns.pairplot(iris_data, hue='Species', vars=['Sepal Lenght'], height=7)
plt.suptitle('Figure 1.1: KDE of Sepal Lenght versus Sepal Lenght', fontsize=10)
plt.savefig('Figure 1.1. KDE of Sepal Lenght.png')
plt.close()

sns.pairplot(iris_data, hue='Species', vars=['Sepal Width'], height=7)
plt.suptitle('Figure 1.2: KDE of Sepal Width versus Sepal Width', fontsize=10)
plt.savefig('Figure 1.2. KDE of Sepal Width.png')
plt.close()

sns.pairplot(iris_data, hue='Species', vars=['Petal Lenght'], height=7)
plt.suptitle('Figure 1.3: KDE of Petal Lenght versus Petal Lenght', fontsize=10)
plt.savefig('Figure 1.3. KDE of Petal Lenght.png')
plt.close()

sns.pairplot(iris_data, hue='Species', vars=['Petal Width'], height=7)
plt.suptitle('Figure 1.4: KDE of Petal Width versus Petal Width', fontsize=10)
plt.savefig('Figure 1.4. KDE of Petal Width.png')
plt.close()


## scatterplot of each pair of variables segregated by species into different colours
# x is x axis data, y is y axis data, hue allows us to differentiate based on the 'species'
# data is taken from original file iris_data
# height and aspect altered from 5 and 1 respectively to alter the image output
# the plt.suptitle adds the title to the graph https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.suptitle.html
# manger = plt.get_current figure, manager.window.showMaximised() makes the new figure pop up in full screen mode
# ref for this is https://stackoverflow.com/questions/32428193/saving-matplotlib-graphs-to-image-as-full-screen
# ref for figuring the graphs https://seaborn.pydata.org/generated/seaborn.catplot.html
# set style 'ticks' makes the images easier to read by increasing the contrast of the points, allegedly

sns.set_style('ticks')

sns.catplot(x='Petal Lenght',y='Petal Width',hue='Species', data=iris_data, height=7, aspect=1.25)
plt.suptitle('Figur 2.1: Petal Lenght versus Petal Width')
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.show()

sns.catplot(x='Petal Lenght',y='Sepal Width',hue='Species', data=iris_data, height=7, aspect=1.25)
plt.suptitle('Figure 2.2: Petal Lenght versus Sepal Width')
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.show()

sns.catplot(x='Petal Lenght',y='Sepal Lenght',hue='Species', data=iris_data, height=7, aspect=1.25)
plt.suptitle('Figure 2.3: Petal Lenght versus Sepal Lenght')
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.show()

sns.catplot(x='Petal Width',y='Sepal Width',hue='Species', data=iris_data, height=7, aspect=1.25)
plt.suptitle('Figure 2.4: Petal Width versus Sepal Width')
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.show()

sns.catplot(x='Petal Width',y='Sepal Lenght',hue='Species', data=iris_data, height=7, aspect=1.25)
plt.suptitle('Figure 2.5: Petal Width versus Sepal Lenght')
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.show()

sns.catplot(x='Sepal Lenght',y='Sepal Width',hue='Species', data=iris_data, height=7, aspect=1.25)
plt.suptitle('Figure 2.6: Sepal Lenght versus Sepal Width')
manager = plt.get_current_fig_manager()
manager.window.showMaximized()
plt.show()