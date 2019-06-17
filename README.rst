<<<<<<< HEAD
===================
Geologic Digitizer
===================
-------------------
June 2019
-------------------

.. image:: logo.png
    :scale: 100%
    :align: center
=======
.. image:: logo.png

#Geologic Digitizer
#18 June 2019
>>>>>>> e0dab332d8c0df97a71515ac7d3eb6547df09c9f

This is a geologic digitizer created by computer science students Marcelo
Gonzales, Jessy Liao, Alexis Ludeman, and Courtney Richardson from the
Colorado School of Mines for the geology department at their school.

<<<<<<< HEAD
--------------------------------------------------------------------------

**INSTRUCTIONS**

The purpose of this program is to make it easier to digitize geologic graphic
logs.  Steps to operate the program are listed below:

1. Select an image of a graphic log to edit

2. Use the toolbar at the top of the page to select brush size, brush color, or eraser

3. Once done editing, select 'Reprune'

4. After final edits and repruning is complete, select 'Output CSV' to export your graphic log to a CSV file.


5. Once the CSV file is saved, you will have the option to digitize a new  log.  Simply click 'Digitize Again', and you will be brought back to the main page where you can select your next image for edit.


While in the editor, you can select a new image to edit by clicking 'Select'.
You must click on 'Next' to begin.

--------------------------------------------------------------------------

**BACKGROUND**

"Graphic logs are the most common way of characterizing sedimentary geologic
rock formations in outcrop and core data.  The term graphic log originates
from a geologist measuring and drawing graphically, or "logging", a cored or
outcropping stratigraphic section.  Graphic logs generally have thickness/depth
on the y axis, and grain size on the x axis.  Many geologists spend weeks in
the field carefully measuring and logging rock formations at fine-scale in an
analog, hand-drawn manner. The fine-scale thickness and grain-size data that
may have taken days or weeks to collect is often never captured digitally in a
tabular format that can be analyzed. So, while tens of thousands of meters of
graphic logs measured at fine-scale exist to quantify various geological parameters,
the data contained in the graphic logs is rarely digitized and available for use.

While software solutions exist to collect graphic log data in the field there
are thousands of hand-drawn logs that need to be digitized.  This project aims to
create an executable where a geologist can digitize the rock layers from a hand-
drawn graphic log.

We hope that the open-source release of this executable will spur the collection of
quantified, structured, and comparable data that, with continued advances in the
accessibility of machine-learning to geologists, will lead to new discoveries
in sedimentary geology." - Zane Jobe

--------------------------------------------------------------------------

**OVERVIEW**

=======
##========================== INSTRUCTIONS ==========================
The purpose of this program is to make it easier to digitize geologic graphic
logs.  Steps to operate the program are listed below:
    1. Select an image of a graphic log to edit
    2. Use the toolbar at the top of the page to select brush size, brush color,
       or eraser
    3. Once done editing, select 'Reprune'
    4. After final edits and repruning is complete, select 'Output CSV' to export
       your graphic log to a CSV file.
    5. Once the CSV file is saved, you will have the option to digitize a new
       log.  Simply click 'Digitize Again', and you will be brought back to the
       main page where you can select your next image for edit.

While in the editor, you can select a new image to edit by clicking 'Select'.
You must click on 'Next' to begin.

##=========================== BACKGROUND ===========================
"Graphic logs are the most common way of characterizing sedimentary geologic
rock formations in outcrop and core data.  The term graphic log originates
from a geologist measuring and drawing graphically, or ‘logging’, a cored or
outcropping stratigraphic section.  Graphic logs generally have thickness/depth
on the y axis, and grain size on the x axis.  Many geologists spend weeks in
the field carefully measuring and logging rock formations at fine-scale in an
analog, hand-drawn manner. The fine-scale thickness and grain-size data that
may have taken days or weeks to collect is often never captured digitally in a
tabular format that can be analyzed. So, while tens of thousands of meters of
graphic logs measured at fine-scale exist to quantify various geological parameters,
the data contained in the graphic logs is rarely digitized and available for use.

While software solutions exist to collect graphic log data in the field there
are thousands of hand-drawn logs that need to be digitized.  This project aims to
create an executable where a geologist can digitize the rock layers from a hand-
drawn graphic log.

We hope that the open-source release of this executable will spur the collection of
quantified, structured, and comparable data that, with continued advances in the
accessibility of machine-learning to geologists, will lead to new discoveries
in sedimentary geology." - Zane Jobe

##============================ OVERVIEW ============================
>>>>>>> e0dab332d8c0df97a71515ac7d3eb6547df09c9f
This program allows the user to choose an image from their computer, edit the
image, and then get it traced and pruned so that the outline of the graph is
saved in a CSV file through its x and y coordinates.  The user will have the
option to reload images, and erase or draw lines so that the CSV matches as
closely as possible to the real core sample of rock.  This program can be used to
digitize legacy data, or keep new data up to date.  This is intended to be open-
sourced as there were many features that could not be implemented in the time
provided for the original project.  The goal is for this program to adapt and
evolve into an extremely useful piece of equipment for geologist around the world.

<<<<<<< HEAD
--------------------------------------------------------------------------

**MAIN FUNCTIONALITY**

canvas_draw.py
    Draws the GUI window and sets buttons and their functionality.  Contains
    definitions to listen to mouse click events and what to do after the mouse is
    clicked.

csv_creation.py
    Reads the image and exports a CSV file to match the coordinates of each layer.

digitizer_v2.py
    Sets up the rest of the GUI, creating buttons that align with the
    functionality given from other classes and definitions.

layer.py
    Getter and setter for creating each layer contained in the CSV file.

plotter.py
    Takes in a CSV file and plots the coordinates given. It then graphs the
    coordinates using mathplotlib, and exports the graph as a PNG file.

--------------------------------------------------------------------------

**INSTALLATION**

=======
##======================== MAIN FUNCTIONALITY ========================
canvas_draw.py:
    - Draws the GUI window and sets buttons and their functionality.  Contains
    definitions to listen to mouse click events and what to do after the mouse is
    clicked.

csv_creation.py:
    - Reads the image and exports a CSV file to match the coordinates of each layer.

digitizer_v2.py:
    - Sets up the rest of the GUI, creating buttons that align with the
    functionality given from other classes and definitions.

layer.py:
    - Getter and setter for creating each layer contained in the CSV file.

plotter.py:
    - Takes in a CSV file and plots the coordinates given. It then graphs the
    coordinates using mathplotlib, and exports the graph as a PNG file.

##=========================== INSTALLATION ===========================
>>>>>>> e0dab332d8c0df97a71515ac7d3eb6547df09c9f
1. The Github repo is hosted at https://github.com/magonzal/CSMJobe. In a Linux
   environment, open the terminal and change directories to where you want the
   packaged cloned using the command: git clone https://github.com/magonzal/CSMJobe
2. The next step is to simply type in the same folder the repo was forked
<<<<<<< HEAD
   'pip install -r requirements.txt' without the quotation marks.
=======
   “pip install -r requirements.txt” without the quotation marks.
>>>>>>> e0dab332d8c0df97a71515ac7d3eb6547df09c9f
3. The final step is to simply type in the same folder python3 digitizer_v2.py to
   run the software.
