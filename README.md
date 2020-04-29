# pands-project
Assignment


My project dowloads data from Fisher's Iris Data, in this case saved as iris.csv file.
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

By using the program I have developed for this assignemtn we generate a summary of each charateristic, in this case; 
Sepal Lenght, Sepal Width, Petal Lenght and Petal Width.
By analysing these summaries, we get a general overview of the data presented to us.
We are provided with data relative to each variable such as their mean, standard deviation, max and min values.
From viewing Table 2. The summary of the Sepal Width, we have determined the standard deviation result to be 0.433594.
This low a result in comparison with the largest, 1.764420 for Petal Lenght Table 3, signifies the relative small difference in the results accross all three species for sepal width.
Thus, it appears that while sepal width will not be a good charaterisation for differentiating the species, petal lenght will be the ideal candidate to best charaterise a given iris with a species.
From Tables 1, and 4, Sepal Lenght and Petal Width, we get figures for standard deviation of approximately 0.7 and 0.8.
This figures show that we can expect some but not great seperation present within our samples and I expect these measurements to help only slightly in the determination of the species during further analysis.

The next output my program generates is a Kernal Density Estimation graph for each variable, however this time, we add in the differentiating factor of Species.
Each file will be saved to the current folder andd thus when they are opened we cand determine thier properties.
From Figure 1.1: KDE of Sepal Lenght, it is imediately clear that the Setosa in blue is well defined compared to the relatively bunched Veriscolour and Virginica.
This is the first clear variable that can be measured to determine at least one of the plants species. That if the sepal lenght is in the range of 4 to 6 cm but primarily roughly 5 cm in lenght we can determine it tp be most certainly of the setosa variant.
This image however does not adequately differentiate the veriscolour and virginica species.
Figure 1.2, KDE of Sepal width is too cloesly packed to be any use of determineing a given species, going against what was determined in section 1 where from the summary we estimated it would be of some value.
From Fugure 1.3. KDE of Petal Lenght, it clearly seperates the setosa in blue from the veriscolour in orange and the virginica in green.
This is no another way along with sepal lenght that we can determine if a species is setosa or not.
This is also the first time we see any speration amongst the other two species.
But, the only conclusion we can derive for justification of the species is that veriscolour will have tend to have the shorter petals than the corresponding virginica.










[1]. Fishers original Iris Data: https://sci-hub.tw/10.1111/j.1469-1809.1936.tb02137.x
