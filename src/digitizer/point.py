#!/usr/bin/env python

#######################################################################################
# Name:         Point 
#
# Last Updated: 5/18/19
#
#######################################################################################


class Point:

    def __init__(self, x, y):
        """

        :param x:
        :param y:
        """
        self._x = x
        self._y = y

    @property
    def x(self):
        """

        :return:
        """
        return self._x

    @property
    def y(self):
        """

        :return:
        """
        return self._y

    @x.setter
    def x(self, x):
        """

        :param x:
        :return:
        """
        self._x = x

    @y.setter
    def y(self, y):
        """

        :param y:
        :return:
        """
        self._y = y
