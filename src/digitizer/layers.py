#!/usr/bin/env python

##############################################################################
# Name:         Layers 
#
# Last Updated: 6/12/19
#
##############################################################################
import sys

class Layers:


    def __init__(self, layer_id):
        self.layer_id = layer_id # serial id of layer (Cannot reset it)
        self._layer_name = str(layer_id) # name of the layer
        self._points = [] # array of point objects 
        self._covered = False # determine if segment of outcrop is usable

    # Getter functions

    @property
    def layer_name(self):
        return self._layer_name

    @property
    def points(self):
        return self._points

    @property 
    def covered(self):
        return self._covered

    # Setter functions

    @layer_name.setter
    def layer_name(self, name):
        self._layer_name = name

    @points.setter
    def points(self, points):
        self._points = points

    @covered.setter
    def covered(self, covered):
        self._covered = covered
    
