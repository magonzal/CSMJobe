#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from numpy import ma
from matplotlib import scale as mscale
from matplotlib import transforms as mtransforms
from matplotlib import rcParams
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


def plotter(current_layer_number):
    current_layer = pd.DataFrame(log_data)
    current_layer = current_layer[current_layer.Layer == current_layer_number]
    plt.xticks([])
    plt.yticks([])
    plt.xlabel("Grain Size")
    plt.ylabel("Depth")
    plt.plot(current_layer.x, current_layer.y, color='black', linewidth=5.0)


# In[3]:


# Getting initial log data from a csv file using pandas

log_data = pd.read_csv('woop.csv')


# In[4]:


# print(log_data.columns)
log_data.head(0)

#Getting total number of layers to graph in order
layer_count = 0
for layer in log_data.Layer:
    if (layer>layer_count):
        layer_count=layer
        
for layer_number in range(layer_count):
    plotter(layer_number+1)

#Export the image to a png file, with a transparent background
plt.savefig('log_data.png', transparent='true', dpi=800)


# In[ ]:





# In[ ]:




