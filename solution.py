"""
Solution to the Sudoku assignment
"""

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [s + t for s in A for t in B]

rows = 'ABCDEFGHI'
cols = '123456789'

boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
diagonals = [['A1', 'B2', 'C3', 'D4', 'E5', 'F6', 'G7', 'H8', 'I9'],
        ['A9', 'B8', 'C7', 'D6', 'E5', 'F4', 'G3', 'H2', 'I1']]

unitlist = row_units + column_units + square_units + diagonals
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

assignments = []

def get_units_for_box(box):
    """
    for a given box return three separate arrays representing the units
    a box belong to
    """
    r, c = box[0], box[1]
    return (cross(r, cols), cross(rows, c),
            [cross(x, y)
                for x in ['ABC', 'DEF', 'GHI'] if r in x
                for y in ['123', '456', '789'] if c in y])

def get_peers_for_box(box):
    """
    for a given box, return peers, including the box itself
    """
    r, c = box[0], box[1]
    return set(cross(r, cols) + cross(rows, c) + [cross(x, y)
        for x in ['ABC', 'DEF', 'GHI'] if r in x for y in ['123', '456', '789'] if c in y][0])

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    # Find all instances of naked twins
    # I have to admit there must be more elegant ways to resolve this, but it works.
    for unit in unitlist:
        # there have to be at least two boxes with a value of length 2 to have naked twins
        peer_boxes = [(values[box], box) for box in unit if len(values[box]) == 2]
        if len(peer_boxes) == 2:
            box1, box2 = peer_boxes[0], peer_boxes[1]
            if box1[0] == box2[0]:
                for u in unit:
                    if len(values[u]) > 2:
                        # Eliminate the naked twins as possibilities for their peers
                        n, t = box1[0][0], box1[0][1]
                        assign_value(values, u, values[u].replace(n, ''))
                        assign_value(values, u, values[u].replace(t, ''))
    return values


def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    values = {}
    grid = [g if g is not '.' else '123456789' for g in grid]
    counter = 0
    for b in boxes:
        assign_value(values, b, grid[counter])
        counter += 1
    return values

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    # this is from the lessons
    width = 1 + max(len(values[s]) for s in boxes)
    line = '+'.join(['-' * (width * 3)] * 3)
    for r in rows:
        print(''.join(values[r + c].center(width) + ('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

def eliminate(values):
    # this is my own implementation from the lessons exercises
    for k in values:
        peers = get_peers_for_box(k)
        for box in peers:
            if len(values[k]) == 1 and values[k] in values[box] and len(values[box]) > 1:
                new_val = values[box].replace(values[k], '')
                assign_value(values, box, new_val)
    return values

def only_choice(values):
    # I also took this from the lesson, my implementation was just as effective but this is cleaner
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                assign_value(values, dplaces[0], digit)
    return values

def reduce_puzzle(values):
    """
    Reduce the puzzle
    Args:
        values(dict): the sudoku in dictionary form
    Returns:
        A grid in dictionary form:
            Keys: the boxes
            Boxes: the values
    """
    # at first i tried resolving the puzzle with just eliminate(only_choice(values))
    # this would work in 12 passes, however naked_twins is required so i use only_choice/eliminate
    # until i get any pair of boxes with 2-length values, so i can attempt naked_twins
    while True:
        newgame = values.copy()
        newgame = eliminate(newgame)
        newgame = only_choice(newgame)
        reduced_boxes = [(len(newgame[box]), newgame[box], box) for box in units if len(newgame[box]) > 1]
        # switch to naked twins strategy if potential naked twins are found
        if len(reduced_boxes) > 1 and min(reduced_boxes)[0] == 2:
            newgame = naked_twins(newgame)
        if max((len(newgame[box]), box) for box in newgame) == 1:
                break
        if newgame == values:
            break
        else:
            values = newgame
    return values

def search(values):
    return values

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = grid_values(grid)
    values = reduce_puzzle(values)
    return values

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except Exception as err:
        print(err)
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
        raise
