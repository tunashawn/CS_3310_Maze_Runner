from func import get_neighbor


def breadth_first_search(m, start, goal):
    """Use Breadth First Search Algorithm to find the path from START to GOAL
        Input: a maze
        Output:
        * path: a path from START to GOAL
        * visited: list of all visited cells"""
    frontier = [start]
    visited = [start]

    # The pyamaze library does not support cell relationships
    # So I use a dictionary to track the parent of the cells
    parent_list = {}

    found = False
    while len(frontier) > 0 and not found:
        cell = frontier.pop(0)
        visited.append(cell)

        # Finding neighbor cells
        for d in 'NWES':
            # A cell has 4 direction East, West, North, and South
            # If the direction has a wall prevent agent to move
            # Then the value of that direction is False, else True
            if m.maze_map[cell][d]:
                neighbor = get_neighbor(d, cell)
                if neighbor in visited or neighbor in frontier:
                    continue

                frontier.append(neighbor)
                # Set parent of this neighbor to the current cell
                parent_list[neighbor] = cell

                if neighbor == goal:
                    found = True
                    break

    # Trace back from the goal to the START cell
    path = {}
    cell = goal
    while cell != start:
        path[parent_list[cell]] = cell
        cell = parent_list[cell]

    return path, visited
