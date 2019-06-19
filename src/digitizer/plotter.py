#This class takes in a CSV file and, plots, and exports a PNG file.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from numpy import ma

#Plotter function that will draw each layer on top of the other on the same plot
class Plotter:
    def __init__(self, log_data, file_name = 'log_data.png'):
        self.log_data = pd.read_csv(log_data)
        self.log_data.head(1)
        self.file_name = file_name

    def getLayers(self):
        layer_count = 0
        for layer in self.log_data.Layer:
            if(layer>layer_count):
                layer_count=layer
        for layer_number in range(layer_count):
            self.plotter(layer_number)
        self.returnImage()
        return self.file_name

    def plotter(self, current_layer_number):
        current_layer = pd.DataFrame(self.log_data)
        current_layer = current_layer[current_layer.Layer == current_layer_number]
        plt.xticks([])
        plt.yticks([])
        plt.plot(current_layer.x, current_layer.y, color='green', linewidth=5.0)

    def returnImage(self):
        plt.savefig(self.file_name, transparent='true')
