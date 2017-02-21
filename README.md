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

