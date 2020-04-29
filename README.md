# pands-project
Assignment


My project dowloads data from Fisher's Iris Dataset, in this case saved as iris.csv file.
It then determines a summary of each given vairable;
Sepal Lenght, Sepal Width, Petal Lenght and Petal Width.
My project saves each of these descriptions as a text file in the current directory.
My program then takes the data and saves an out put of each vaiable menitoned above in the form of a Kernal density estimation.png file.
These however, are also sepperated into their respective species; Setosa, Veriscolour and Virginica.
These png files are also saved in the current directory.
Finally, my program opens up scatter plots of two variables against each other, in  total 6.
These open maximised to the screen, one openeing as the prior one is closed.



Fisher's Iris Dataset Investigation

Fisher's Iris Dataset consists of information taken from three different iris species.
Fifty of each species, Setosa, Veriscolour and Virginica were measured for certain criteria to deterine their anatomy of each plant.
The measurements he took, all in cm, showed the differences between the lenghts and widths of the sepal and petal of each plant.
The data is recorded in his paper from 1936 and it is this data we will be investiagting. [1]

By using the program I have developed for this assignment we generate a summary of each charateristic, in this case; 
Sepal Lenght, Sepal Width, Petal Lenght and Petal Width.
By analysing these summaries, we get a general overview of the data presented to us.
We are provided with data relative to each variable such as their mean, standard deviation, max and min values.
From viewing Table 2. The summary of the Sepal Width, we have determined the standard deviation result to be 0.433594.
This low a result in comparison with the largest, 1.764420 for Petal Lenght Table 3, signifies the relative small difference in the results accross all three species for sepal width.
Thus, it appears that while sepal width will not be a good charaterisation for differentiating the species, petal lenght will be the ideal candidate to best charaterise a given iris with a species.
From Tables 1, and 4, Sepal Lenght and Petal Width, we get figures for standard deviation of approximately 0.7 and 0.8.
This figures show that we can expect some but not great seperation present within our samples and I expect these measurements to help only slightly in the determination of the species during further analysis.

The next output my program generates is a Kernal Density Estimation graph for each variable, however this time, we add in the differentiating factor of Species.
Each file will be saved to the current folder andd thus when they are opened we can determine thier properties.
From Figure 1.1: KDE of Sepal Lenght, it is immediately clear that the Setosa in blue is well defined compared to the relatively bunched Veriscolour and Virginica.
This is the first clear variable that we have measured to determine at least one of the plants species. That if the sepal lenght is in the range of 4 to 6 cm but primarily roughly 5 cm in lenght we can determine it t0 be most certainly of the setosa variant.
This image however does not adequately differentiate the veriscolour and virginica species.
Figure 1.2, KDE of Sepal width is too cloesly packed to be any use of determineing a given species, going against what was determined in section 1 where from the summary we estimated it would be of some value.
All three peaks correspond to approximately 3cm and thus can not be considered an adequate seperating factor.
From Fugure 1.3. KDE of Petal Lenght, it clearly seperates the setosa in blue from the veriscolour in orange and the virginica in green.
This is now another way along with sepal lenght that we can determine if a species is setosa or not.
The setosa petal lenght will primarily be 1 to 2 cm in lenght while veriscolour will be 4 and virginica 5.5cm in lenght respectively.
This is also the first time we see any speration amongst the other two species.
But, the only conclusion we can derive for justification of the species is that veriscolour will have tend to have the shorter petals than the corresponding virginica.
Figure 1.4. KDE of Petal Width, gives us yet another clear view of how to determine the species setosa from the vericolour and virginica.
However, it also seperates the veriscolour and the virginica enough to be able to determine that veriscolour would have the smaller petal widths in comparison to the more wider petal virginica species.
The setosa plant is exclusively present within 0.0 and 0.7 cm in petal width, while the range for veriscolour is 0.7 - 2.1 and virginica is 1.0 - 2.9.
We again have no definitive way of determining the difference between the veriscolour and the virginica species, however, we can say that the petal width for versicolour should be smaller than that of virginica.

The final part of the program automatically opens up scatter plots of given variables.
In the first of which, Figure 2.1. Petal Lenght versus Petal Widht, it begins to become clear the differnces between the three species.
Setosa, in blue, again is distinctly obvious from the other two species, this time in the bottom left corner with the lower petal lenght and widths.
The veriscolour is primarily in the centre of the graph in orange while the virginica dominates the upper right quadrant of the graph with both the largest petal lenght and patal width.
Figure 2.2. petal lenght versys sepal width, Figure 2.3. petal lenght versus sepal lenght, Figure 2.4. Petal Width versus Sepal Width Figure 2.5. Petal Width versus Sepal Lenght, all have similar properties clearing seperating the species based on the two variables present.
The only scatter plot that fails to adequately distinguish the species is Figure 2.6. Sepal Lenght versus Sepal Width.
Here we again get a cluster of setosa in the top left corner this time, however the verisolour and virginica are spread out accross the rest of the graph.
This is the only pair of variables that show a clear relationship between two variables to determine what species a given iris plant belongs to.

From my analysis of the Fisher Iris Data Set it can be determined that it is relatively simple to classify a sample as setosa based on one variable.
However, if you wish to determine whether it is veriscolour or virginica then it requires the ability to graph two variables to determine the species present.
Veriscolour will be smaller on most variables with respect to the virginica while both species are larger than the setosa species.

Thank you.










[1]. Fishers original Iris Data: https://sci-hub.tw/10.1111/j.1469-1809.1936.tb02137.x
