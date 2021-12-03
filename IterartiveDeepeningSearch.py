import random

from func import get_neighbor


def iterative_deepening_search(m, start, depth_limit):
    """Use Random Depth First Search Algorithm to find the path from START to GOAL
    NOTE: This function can only work with a perfect maze
    Input:
    * m: a maze
    * start: position of the agent
    * depth_limit: limit on depth
    Output:
    * path: a path from START to GOAL
    * visited: list of all visited cells"""
    depth_count = 0
    frontier = [(depth_count, start)]
    visited = [start]

    # The pyamaze library does not support cell relationships
    # So I use a dictionary to track the parent of the cells
    parent_list = {}

    directions = ['N', 'E', 'W', 'S']

    found = False
    while len(frontier) > 0 and not found:
        frontier.sort(key=lambda x: x[0])
        c = frontier.pop(0)
        cell = c[1]

        # Shuffle the directions so that
        # the agent won't go in a specific direction on the maze
        random.shuffle(directions)

        depth_count = c[0] + 1

        if depth_count > depth_limit:
            continue

        visited.append(cell)

        # Finding neighbor cells
        for d in directions:
            # A cell has 4 direction East, West, North, and South
            # If the direction has a wall prevent agent to move
            # Then the value of that direction is False, else True
            if m.maze_map[cell][d]:
                neighbor = get_neighbor(d, cell)
                if neighbor in visited or neighbor in frontier:
                    continue

                frontier.append((depth_count, neighbor))
                # Set parent of this neighbor to the current cell
                parent_list[neighbor] = cell

                if neighbor == m._goal:
                    found = True
                    break

    # Trace back from the goal to the START cell
    path = {}
    if found:
        cell = m._goal
        while cell != start:
            path[parent_list[cell]] = cell
            cell = parent_list[cell]

    return path, visited
