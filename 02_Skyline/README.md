# Skyline Problem
Given n rectangular buildings in a 2-dimensional city, computes the skyline of these buildings, eliminating hidden lines. The main task is to view buildings from aside and remove all sections that are not visible. 

All buildings share a common bottom and every building is represented by a triplet (h, Lxi, Rxi) 

h: is the height of the building.
Lxi: is x coordinated on the left side (or wall)
Rxi: is x coordinate of the right side.

A skyline is a collection of rectangular strips. A rectangular strip is represented as a pair (h, Lxi) where left is x coordinate of the left side of the strip and h is the height of the strip.

## Overview
This project implements a divide-and-conquer approach to the Skyline Problem, wherein we are given a series of tuples representing buildings, and asked to provide the points representing the merged "skyline" created by the inputted buildings. It has a time complexity of O(nlogn).

## Problem Statement
The code assumes that we will be given the buildings in a series of tuples of form (h, Lxi, Rxi) where h is building height, Lxi is x value of the starting point of the building's roof, Rxi is the xvalue of the ending point of the building's roof.
All roofs are horizontal. 
The output will be a series of coordinate pairs in form (h, x). These points represent the starting points of the lines making up the roofs in the "merged" skyline.

The merged skyline only includes the exterior-most parts of the building silhouettes. For example, if a building completely overlaps a smaller building, the merged skyline would ONLY include the larger building. If a building overlaps another building, any overlapped points will be excluded from the merged skyline.

## Features
- Handles any number of buildings
- Handles edge cases where
      - Buildings of different heights start at same point on x-axis.
      - Several buildings are arranged in a "stairstep" pattern with the starting point of a building being contained within the building before it.
      - Several buildings in a row where a building begins where the previous one ends


## Implementation Details

### Input Format
- File format: Text or CSV file 
- Building Values: comma seperated non-negative integers of the form (h, Lxi, Rxi)
Example: buildings = [(6, 1, 6) , (8, 3, 5) , (4, 4, 9) , (2, 7, 12) , (7, 11, 14)]
### Output Format
- Outline Values: comma seperated coordinates of the form (h, x) for each building in a new line
Example: outline = [(6, 1) , (8, 3) , (6, 5) , (4, 6) , (2, 9) , (7, 11) , (0, 14)]

## Running the code
- Add .txt/.csv file in InputsOutputs folder
- InputsOutputs folder has some sample data (with numbers as suffix) which we tested with. Files with suffix (_e1, e2,..) are error cases.
- Change the file path in path variable under main()
- Run the skyline.py
- Output will be saved under InputsOutputs folder as 'Output{file_num_suffix}.txt'


## Team members
- Ryan Howington - rhowing4@students.kennesaw.edu
- Sai Sruti Dandibhatla - sdandib1@students.kennesaw.edu
- Pradyumna Kumar - pkumar7@students.kennesaw.edu
