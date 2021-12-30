from func import estimated_cost, get_neighbor


def a_star_search(m, start):
    """Use A* Search Algorithm to find the path from START to GOAL
    Input: a maze and the position of agent
    Output:
    * path: a path from START to GOAL
    * visited: list of all visited cells"""
    cost_to_reach = 0
    total_cost = cost_to_reach + estimated_cost(start, m._goal)
    frontier = [(total_cost, cost_to_reach, start)]
    visited = [start]

    # frontier_list contains all visited cells and cells in frontier
    # just to make it easier to check whether to add the cells to frontier or not
    frontier_list = [start]

    # The pyamaze library does not support cell relationships
    # So I use a dictionary to track the parent of the cells
    parent_list = {}

    found = False

    while len(frontier) > 0 and not found:
        frontier.sort(key=lambda x: x[0])
        x = frontier.pop(0)
        cell = x[2]
        visited.append(cell)

        # Increase cost to reach this cell
        cost_to_reach = x[1] + 1

        # Finding neighbor cells
        for d in 'NWES':
            # A cell has 4 direction East, West, North, and South
            # If the direction has a wall prevent agent to move
            # Then the value of that direction is False, else True
            if m.maze_map[cell][d]:
                neighbor = get_neighbor(d, cell)

                if neighbor in frontier_list:
                    continue

                # Calculate the total cost = h(n) + g(n)
                total_cost = cost_to_reach + estimated_cost(neighbor, m._goal)

                frontier.append((total_cost, cost_to_reach, neighbor))
                frontier_list.append(neighbor)
                # Set parent of this neighbor to the current cell
                parent_list[neighbor] = cell

                if neighbor == m._goal: # Break the loop if found the GOAL
                    found = True
                    break

    # Trace back from the goal to the START GOAL
    path = {}   # Store path from START to GOAL
    cell = m._goal
    while cell != start:
        path[parent_list[cell]] = cell
        cell = parent_list[cell]
        
    return path, visited
