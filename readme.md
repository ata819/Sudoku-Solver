Owner: Alan Ta
Language: Python
Date: 02/13/20

Overview: this is a simple Sudoku solver. I decided to make to do this project becuase I want to get more familar with python. Its does not have a GUI so it will just printout to stdout, though maybe a GUI project might be coming soon.

This solver uses back tracking in order to find the correct postion for all the blank spaces. Backtracking was an interesting algorithm to understand. Its a recursive algorithm and goes through each position and attempts to find the correct number order for the rows, columns, and 3x3 quadrant. It goes through and tests out each possible number and if it reaches a point where the possible arrangement fails, its will "backtrack" and clear the incorrect number and try again. 

