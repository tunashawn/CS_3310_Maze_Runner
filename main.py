from pyamaze import *
from AStarSearch import a_star_search
from BreadthFirstSearch import breadth_first_search
from RandomizedDepthFirstSearch import randomized_depth_first_search


# The organization of cells is like this
# Use it to change coordinates of START and GOAL
#   (1,1)   (1,2)   (1,3)
#   (2,1)   (2,2)   (2,3)
#   (3,1)   (2,2)   (3,3)

HEIGHT = 60 # Number of cells on vertical line
WIDTH = 60  # Number of cells on horizontal line

START = (30, 30)    # Start point of the agent
GOAL = (49, 59)     # Goal to reach

# 0 means perfect maze
# Increase to have more loops on the maze
LOOP_PERCENTAGE = 50


def menu():
    m = maze(HEIGHT, WIDTH)

    # Use this to load the perfect maze
    # delete loadMaze to get a random maze instead
    # m.CreateMaze(GOAL[0], GOAL[1], loadMaze='perfect_maze.csv', theme=COLOR.light)

    # Use this to load the non perfect maze "maze1.csv"
    # delete loadMaze to get a random maze instead
    m.CreateMaze(GOAL[0], GOAL[1], loopPercent=LOOP_PERCENTAGE, loadMaze='maze1.csv', theme=COLOR.light)

    # Creating agents
    a = agent(m, x=START[0], y=START[1], goal=GOAL, footprints=True, color=COLOR.blue, filled=True)
    b = agent(m, x=START[0], y=START[1], goal=GOAL, footprints=True, color=COLOR.yellow, filled=True)
    c = agent(m, x=START[0], y=START[1], goal=GOAL, footprints=True, color=COLOR.red)

    dfs_path, dfsvisited = randomized_depth_first_search(m, START, GOAL)
    bfs_path, bfsvisited = breadth_first_search(m, START, GOAL)
    ass_path, assvisited = a_star_search(m, START, GOAL)

    # RUN ONLY ONE FROM BELOW CODES

    # To run Randomized Depth First Search
    m.tracePath({a: dfs_path}, delay=15)
    l1 = textLabel(m, 'Total cells explored', len(dfsvisited))
    l2 = textLabel(m, 'Path length', len(dfs_path))

    # To run Breadth First Search
    # m.tracePath({b: bfs_path}, delay=15)
    # l1 = textLabel(m, 'Total cells explored', len(bfsvisited))
    # l2 = textLabel(m, 'Path length', len(bfs_path))

    # To run A* Search
    # m.tracePath({c: ass_path}, delay=15)
    # l1 = textLabel(m, 'Total cells explored', len(assvisited))
    # l2 = textLabel(m, 'Path length', len(ass_path))

    # To compare path from 3
    # m.tracePath({a: dfs_path}, delay=15)
    # m.tracePath({b: bfs_path}, delay=15)
    # m.tracePath({c: ass_path}, delay=15)

    m.run()


def main():
    menu()


if __name__ == '__main__':
    main()
