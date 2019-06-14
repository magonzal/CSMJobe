#This class takes in a CSV file and, plots, and exports a PNG file.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from numpy import ma
from matplotlib import scale as mscale
from matplotlib import transforms as mtransforms
from matplotlib import rcParams
get_ipython().run_line_magic('matplotlib', 'inline')

#Plotter function that will draw each layer on top of the other on the same plot
class plotCreator:
    def __init__(self, log_data):
        self.log_data = pd.read_csv('log_data')
        self.log_data.head(0)

    def getLayers(self, log_data):
        layer_count = 0
        for layer in log_data.Layer:
            if(layer>layer_count):
                layer_count=layer
        for layer_number in range(layer_count):
            plotter(layer_number)
        returnImage()

    def plotter(self, current_layer_number):
        current_layer = pd.DataFrame(self.log_data)
        current_layer = current_layer[current_layer.Layer == current_layer_number]
        plt.xticks([])
        plt.yticks([])
        plt.plot(current_layer.x, current_layer.y, color='black', linewidth=5.0)

    def returnImage(self):
        plt.savefig('log_data.png', transparent='true', dpi=800)
