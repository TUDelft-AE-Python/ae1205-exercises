"""
    Show four flight log files on Google maps window
    May 10th, 2014
    Jacco M. Hoekstra
"""

import numpy as np
import pygmaps
import os

# Lists with log files and corresponding colours
fnames = ["flight1.log", "flight2.log", "flight3.log", "flight4.log"]
colours = ["#FF0000", "#00FF00", "#0000FF", "#00FFFF"]

# Set window position and zoom level
centerlat = 51.85
centerlon = 5.0
zoomlevel = 10

# Define map object
mymap = pygmaps.pygmaps(centerlat, centerlon, zoomlevel)

# Do for all files
for i in range(len(fnames)):

    # Read data    
    fdata = np.genfromtxt(fnames[i], comments="#", skiprows=2)

    # Create path list: (lat1,long1), (lat2,long2)
    path = list(fdata[:, 1:3])

    # Add path to map
    mymap.addpath(path, colours[i])

# Make html file (comparable to pygame.display.flip() or plt.show() )
print("Showing map window...")
mymap.draw("test.html")

# Use os module to start html file
os.system("test.html")
print("Ready.")
