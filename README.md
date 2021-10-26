# Introduction to research skills (for GC)
## Assignment 4: Visualisation of rush hours for the city of Montréal

This repository contains the following files :
* assignement4.py: the python file containing the code to model the traffic congestion
* export_trajets.csv: the CSV containing the data 
* week.jpg and weekend.jpg: which represents the two graphs that you should get after compiling the code

## Data

The initial data can be found at this Url: https://donnees.montreal.ca/ville-de-montreal/mtl-trajet 
* export_trajets.csv: In this file, you will find all the initial data points extracted from the shapefile provided on the website. The CSV consists of 5 different columns: id of the trip, travel mode, purpose, start_time, and end_time
The raw dataset contains about 185’000 rows, where each one represents one trip of a user.

## Description
As the initial data are a Geolocated dataset in a shapefile. It was first needed to convert the data.
So, we used the geographic information system ”QGIS”, which allows us to load a shapefile and export it as a CSV file ("export_trajets.csv").
The second step was to model the traffic congestion of the city of Montreal for the period of September 2017 to October 2017. The code for this part is provided in " assignement4.py". Its output shows that we have three specific rush hours during the week and none during the weekend. It also supports the analysis with two graphs.

Warning: Due to the big amount of data, the code takes 5-7 minutes to run to make both graphs.

## Getting Started

First, you will need to have " git " install on your computer to be able to clone the repository on your computer. You will also need to have python installed. If this is not the case you can download it from here: https://www.python.org/downloads/ 

## Dependencies and Installing

The code is using two Python libraries: "Pandas" to analyze data and "Matplotlib" to visualize the output of the analysis 

If you are completely new to these two libraries. The easiest way to get them is to download "anaconda" to be able to use "conda" command in your terminal. Here is the link: https://docs.anaconda.com/anaconda/install/index.html . Those two can also be downloaded in some other way. More information is provided on their website: https://pypi.org/project/pandas/

If you are using anaconda, you can simply copy those code lines on your terminal.

* pandas : 
```
conda install -c anaconda pandas
```

* matplotlib :

```
conda install matplotlib
```

### Executing program

To execute the program you need to follow the step described below:
* clone the repository 
* Get the Python libraries
* enter in the repository with this command (Windows) or equivalent code line for Mac and Linux
```
cd researchskill_assignement4
```
* and then run the file assignement4.py as follow:
```
python assignement4.py
```
* After 5-6 min, two files should have been saved as 'week.jpg' and 'weekend.jpg'


## Help

If any problem occurs you can contact me on my address email: simon.dayer@gmail.com

## Authors

Simon Dayer

