# -*- coding: utf-8 -*-
"""
Created on Wed May 29 14:39:04 2019

@author: CSM Jobe team

This file contains the set up and functionality contained in the GUI
"""

import tkinter
from tkinter import *
from tkinter import filedialog
import cv2
import os
import io
from PIL import Image, ImageTk, ImageDraw, EpsImagePlugin
import PIL.ImageTk
import PIL.Image
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename
import subprocess

class Gui:
    DEFAULT_PEN_SIZE = 5.0
    line_width = 5.0
    DEFAULT_COLOR = 'black'

    # ------- Initial window setup ------- #
    def __init__(self, window, window_title):

        # Gets the file from users file manager allowing user to pick their own image
        self.filename = askopenfilename()
        self.image_path = cv2.imread(str(self.filename))

        # Creating window
        self.window = window
        self.window.title(window_title)

        # Load an image using OpenCV
        self.cv_img = self.image_path

        # Get the image dimensions (OpenCV stores image data as NumPy ndarray)
        self.height, self.width, no_channels = self.cv_img.shape

        # Create a canvas that can fit the above image
        self.canvas = tkinter.Canvas(window, width=self.width, height=self.height+10)
        self.canvas.pack(side='left')

        # Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.cv_img))

        # Add a PhotoImage to the Canvas
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

        # Button that lets the user draw on the image
        self.pen_button = tkinter.Button(window, text="Pen", command=self.use_pen)
        self.pen_button.pack(side='top', fill='both', expand=False)

        # Button that lets the user erase anything on the image
        self.eraser_button = tkinter.Button(self.window, text="Eraser", command=self.use_eraser)
        self.eraser_button.pack(side='top', fill='both', expand=False)

        # Scale button that lets the user choose their pen size
        self.choose_size_button = Scale(self.window, from_=1, to=10, orient='horizontal')
        self.choose_size_button.pack(side='top', fill='both', expand=False)

        # Button that lets the user choose their pen color
        self.color_button = Button(self.window, text="Color", command=self.choose_color)
        self.color_button.pack(side='top', fill='both', expand=False)

        # Button that lets the user define where the origin is
        self.set_origin_button = Button(self.window, text="Next ->", command=self.changeImg)
        self.set_origin_button.pack(side='top', fill='both', expand=False)

        # Button that user clicks to let the program know they are done with their edits
        self.done_button = tkinter.Button(self.window, text="Done", command=self.save_image)
        self.done_button.pack(side='bottom', fill='both', expand=False)

        # Creates GUI window
        self.setup()
        self.window.mainloop()

    # ------- Callback for setup ------- #
    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.activate_button = self.pen_button
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)

    # ------- Callback for pen use ------- #
    def use_pen(self):
        self.color = 'black'    # Pen color is black
        self.activate_button(self.pen_button)

    # ------- Callback for eraser use ------- #
    def use_eraser(self):
        self.color = 'white'    # Eraser color is white
        self.activate_button(self.eraser_button, eraser_mode=True)

    # ------- Callback for color choice ------- #
    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    # ------- Callback for button activation, to recognize when which button is clicked ------- #
    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief='raised')
        some_button.config(relief='sunken')
        self.active_button = some_button
        self.eraser_on = eraser_mode

    # ------- Callback for updating the image ------- #
    def changeImg(self):
        self.img = PhotoImage(file="log_data.png")
        self.canvas.itemconfig(self.imgArea, image=self.img)

    # ------- Callback for paint ------- #
    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                                    width=self.line_width, fill=paint_color,
                                    capstyle='round', smooth=True, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    # ------- Callback for reset ------- #
    def reset(self, event):
        self.old_x, self.old_y = None, None

    # ------- Callback for saving image, called when 'Done' is clicked ------- #
    def save_image(self):
        # Change filename to match needed format
        self.filename = self.filename[:-3] + "eps"
        self.canvas.postscript(file=self.filename)
        img = Image.open(self.filename)
        # Save image
        img.save("victory.png", "png")

        tkinter.messagebox.askokcancel('!', 'You are now exiting the GUI.  Your updated image has been saved as "victory.png" on your decive.')

        self.window.quit()

