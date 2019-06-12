import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from numpy import ma
from matplotlib import scale as mscale
from matplotlib import transforms as mtransforms
from matplotlib import rcParams
%matplotlib inline

#Function that takes in the current layer and plots the lines onto the same
#plot to view the log from the points.
def plotter(current_layer_number):
    current_layer = pd.DataFrame(log_data)
    current_layer = current_layer[current_layer.Layer == current_layer_number]
    plt.xlabel("Grain Size")
    plt.ylabel("Depth")
    plt.plot(current_layer.x, current_layer.y, color='black', linewidth=5.0)

#Reading in the csv
log_data = pd.read_csv('log.csv')

#Getting total number of layers to graph in order
layer_count = 0
for layer in log_data.Layer:
    if (layer>layer_count):
        layer_count=layer

#For each layer in the log data, call the plotter function
for layer_number in range(layer_count):
    plotter(layer_number+1)

#Export the image to a png file, with a transparent background
plt.savefig('log_data.png', transparent='true', dpi=800)
