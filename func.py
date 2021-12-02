def get_neighbor(d, cell):
    if d == 'E':  # Case neighbor cell is on the right
        neighbor = (cell[0], cell[1] + 1)  # Increase x coordinate
    elif d == 'W':  # Case neighbor cell is on the left
        neighbor = (cell[0], cell[1] - 1)  # Decrease x coordinate
    elif d == 'N':  # Case neighbor cell is up above
        neighbor = (cell[0] - 1, cell[1])  # Decrease y coordinate
    elif d == 'S':  # Case neighbor cell is down below
        neighbor = (cell[0] + 1, cell[1])  # Increase y coordinate
    return neighbor


def estimated_cost(cell1, cell2):
    """Calculate estimated cost from cell 1 to cell 2"""
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1 - x2) + abs(y1 - y2)
