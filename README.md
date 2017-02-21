# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: Each box in the grid belongs to 3 units: the row, the column and the square it's contained in.
No two cells share the same units: this means that by applying the naked_twins strategy to a third box,
at least 1 unit that was not in common with the naked twins pair of boxes will be affected (in the worst case scenario,
e.g. two naked twins in the same row and same square, the affected boxes will be in different columns, but
there are 75% chances of affecting two other units).
Modifying the value of cells that influence a different set of units has the effect of modifying the
constraint satisfaction for those units, in other words, the moment the content of a box is changed through
a naked twins strategy, new constraints are in place for affected units, which must be satisfied.
In example, if boxes A1 and A2 were a naked twin pair, affecting boxes A5 and A8, then the change will have 
propagated constraints into column 5, column 8, square 2 and square 3 (with square 1 being top-left and square 9
bottom-right).

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: If we think of the diagonals as additional units to the game, changing a value in one of the boxes in the 
diagonals will immediately propagate constraints into the box's three other units (row, column, square).
This in fact makes the game easier to solve because the more constraints are enforced, the less potential values
can be contained in a single box.


### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.
