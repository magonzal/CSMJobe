import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from numpy import ma
from matplotlib import scale as mscale
from matplotlib import transforms as mtransforms
from matplotlib import rcParams

#Function that takes in the current layer and plots the lines onto the same
#plot to view the log from the points.


class Plotter:

    def __init__(self, log_data, layer_count=0):
        self.log_data = log_data
        self.layer_count = layer_count
        for layer in log_data.Layer:
            if layer > layer_count:
                self.layer_count = layer

    @property
    def log_data(self):
        return self.log_data

    @property
    def layer_count(self):
        return self.layer_count

    @log_data.setter
    def log_data(self, data):
        self.log_data = data

    @layer_count.setter
    def layer_count(self, count):
        self.layer_count = count

    def _plotter(self, current_layer_number):
        current_layer = pd.DataFrame(self.log_data)
        current_layer = current_layer[current_layer.Layer == current_layer_number]
        plt.xlabel("Grain Size")
        plt.ylabel("Depth")
        plt.plot(current_layer.x, current_layer.y, color='black', linewidth=5.0)

    def plot(self):
        for n in range(self.layer_count):
            self._plotter(n+1)
        plt.savefig('log_data.png', transparent='true', dpi=800)

#Reading in the csv
#log_data = pd.read_csv('log.csv')

#Getting total number of layers to graph in order
#layer_count = 0
#for layer in log_data.Layer:
#    if (layer>layer_count):
#        layer_count=layer

#For each layer in the log data, call the plotter function
#for layer_number in range(layer_count):
#    plotter(layer_number+1)

#Export the image to a png file, with a transparent background
#plt.savefig('log_data.png', transparent='true', dpi=800)
