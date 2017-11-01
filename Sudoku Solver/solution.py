

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """

    # Don't waste memory appending actions that don't actually change any values
    if values[box] == value:
        return values

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
    # Eliminate the naked twins as possibilities for their peers
    possibilities = [box for box in values.keys() if len(values[box]) == 2]

    # assigning all sets of naked twins by comparing it with its peers and if they are equal then append pairs to nakedTwins
    naked_twins = [[b1, b2] for b1 in possibilities for b2 in peers[b1] if values[b1] == values[b2]]

    # going through each pair in nakedTwins
    for b1, b2 in naked_twins:
        # checking to make sure the length of each pair is two
        if len(values[b1]) == 2 and len(values[b2]) == 2:
            d1 = values[b1][0]
            d2 = values[b1][1]
            # grabbing all common peers for the twins
            commons = list(set(peers[b1]) & set(peers[b2]))
            for p in commons:
                # removing the values of the naked twins from all other peers
                # while making sure it does not remove it from the twin itself
                if len(values[p]) > 1 and values[p] != values[b1] and values[p] != values[b2]:
                    values[p] = values[p].replace(d1, '')
                    values[p] = values[p].replace(d2, '')

    # returning values
    return values


def cross(A, B):
    """
    Cross product of elements in A and elements in B.
    """
    return [s+t for s in A for t in B]


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
    chars = []
    digits = '123456789'
    for col in grid:
        if col == '.':
            chars.append(digits)
        if col in digits:
            chars.append(col)
    assert len(chars) == 81
    return dict(zip(boxes, chars))


def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1 + max(len(values[s]) for s in boxes)
    line = '+'.join(['-' * (width * 3)] * 3)
    for r in rows:
        print(''.join(values[r + c].center(width) + ('|' if c in '36' else '')
                      for c in columns))
        if r in 'CF': print(line)

    return


def eliminate(values):
    """
    Args:
        values:
    Returns: deletes the value once a solution to a  box is found

    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            assign_value(values, peer, values[peer].replace(digit, ''))
    return values


def only_choice(values):
    """
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns: returns value of the only valid choice for that box using back prop

    """
    all_digits = '123456789'
    for unit in unit_list:
        for digit in all_digits:
            # get all boxes in the unit that have the digit
            boxes_with_digit = [box for box in unit if digit in values[box]]
            # if there is only 1 box, update it
            if len(boxes_with_digit) == 1:
                assign_value(values, boxes_with_digit[0], digit)

    return values


def reduce_puzzle(values):
    """
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns: a resulting sudoku puzzle is in dictionary form

    """
    stalled = False

    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        values = only_choice(values)
        values = naked_twins(values)

        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])

        stalled = solved_values_before == solved_values_after

        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values


def search(values):
    """
    Args:
        values: values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns: using depth-first search and propagation, it creates a search tree and solves the sudoku puzzle.

    """
    values = reduce_puzzle(values)
    if values is False:
        return False
    # Chose one of the unfilled square s with the fewest possibilities
    unsolved_values = [box for box in values.keys() if len(values[box]) > 1]
    # print(len(unsolved_values))
    if len(unsolved_values) > 0:
        box, vals = sorted(values.items(), key=lambda x: 10 if (len(x[1]) <= 1) else len(x[1]))[0]
        # print(box, vals)
        for v in vals:
            values_try = values.copy()
            assign_value(values_try, box, v)
            # values_try[box] = v
            solve_try = search(values_try)
            if solve_try:
                return solve_try
    else:
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
    values = search(values)

    return values

# Defined Parameters and Global variables
assignments = []
rows = 'ABCDEFGHI'
columns = '123456789'
boxes = cross(rows, columns)
columns_reversed = columns[::-1]

row_units = [cross(r, columns) for r in rows]
column_units = [cross(rows, c) for c in columns]
square_units = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
d1_units = [[rows[i] + columns[i] for i in range(len(rows))]]
d2_units = [[rows[i] + columns_reversed[i] for i in range(len(rows))]]

do_diagnonal = 1

if do_diagnonal == 1:
    unit_list = row_units + column_units + square_units + d1_units + d2_units
else:
    unit_list = row_units + column_units + square_units

units = dict((s, [u for u in unit_list if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s], []))-set([s])) for s in boxes)

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
