from pyamaze import *
from AStarSearch import a_star_search
from BestFirstSearch import best_first_search
from BreadthFirstSearch import breadth_first_search
from IterartiveDeepeningSearch import iterative_deepening_search
from RandomizedDepthFirstSearch import randomized_depth_first_search
from DepthLimitedSearch import depth_limited_first_search

# The organization of cells is like this
# Use it to change coordinates of START and GOAL
#   (1,1)   (1,2)   (1,3)
#   (2,1)   (2,2)   (2,3)
#   (3,1)   (2,2)   (3,3)

HEIGHT = 60 # Number of cells on vertical line
WIDTH = 60  # Number of cells on horizontal line

START = (30, 30)    # Start point of the agent
GOAL = (60, 60)     # Goal to reach

# 0 means perfect maze
# Increase to have more loops on the maze
LOOP_PERCENTAGE = 0
DEPTH_LIMIT = 20

def menu():
    m = maze(HEIGHT, WIDTH)

    # Use this to load the perfect maze
    # delete loadMaze to get a random maze instead
    # m.CreateMaze(GOAL[0], GOAL[1], loadMaze='perfect_maze.csv', theme=COLOR.light)

    # Use this to load the non perfect maze "maze1.csv"
    # delete loadMaze to get a random maze instead
    # IMPORTANT: Size of maze1.csv is 60x60
    m.CreateMaze(GOAL[0], GOAL[1], loadMaze='maze1.csv', theme=COLOR.light)

    # Creating agents
    a = agent(m, x=START[0], y=START[1], footprints=True, color=COLOR.blue, filled=True)
    b = agent(m, x=START[0], y=START[1], footprints=True, color=COLOR.yellow, filled=True)
    c = agent(m, x=START[0], y=START[1], footprints=True, color=COLOR.red)

    dfs_path, dfsvisited = randomized_depth_first_search(m, START)
    bfs_path, bfsvisited = breadth_first_search(m, START)
    ass_path, assvisited = a_star_search(m, START)
    best_part, best_visited = best_first_search(m, START)
    dls_path, dlsvisited = depth_limited_first_search(m, START, DEPTH_LIMIT)
    ids_path, idsvisited = iterative_deepening_search(m, START, DEPTH_LIMIT)


    # RUN ONLY ONE FROM BELOW CODES

    # To run Randomized Depth First Search
    # m.tracePath({a: dfsvisited}, delay=10)
    # m.tracePath({b: dfs_path}, delay=15)
    # l = textLabel(m, 'RUNNING DEPTH FIRST SEARCH','')
    # l1 = textLabel(m, 'Total cells explored', len(dfsvisited))
    # l2 = textLabel(m, 'Path length', len(dfs_path))

    # To run Breadth First Search
    # m.tracePath({a: bfsvisited}, delay=10)
    # m.tracePath({b: bfs_path}, delay=15)
    # l = textLabel(m, 'RUNNING BREADTH FIRST SEARCH', '')
    # l1 = textLabel(m, 'Total cells explored', len(bfsvisited))
    # l2 = textLabel(m, 'Path length', len(bfs_path))

    # To run A* Search
    m.tracePath({a: assvisited}, delay=15)
    m.tracePath({b: ass_path}, delay=15)
    l = textLabel(m, 'RUNNING A* FIRST SEARCH', '')
    l1 = textLabel(m, 'Total cells explored', len(assvisited))
    l2 = textLabel(m, 'Path length', len(ass_path))

    # To compare path from 3 algorithms above
    # m.tracePath({a: dfs_path}, delay=10)
    # m.tracePath({b: bfs_path}, delay=15)
    # m.tracePath({c: ass_path}, delay=15)

    # To run Best First Search
    # m.tracePath({a: best_visited}, delay=10)
    # m.tracePath({b: best_part}, delay=15)
    # l = textLabel(m, 'RUNNING BEST FIRST FIRST SEARCH', '')
    # l1 = textLabel(m, 'Total cells explored', len(best_visited))
    # l2 = textLabel(m, 'Path length', len(best_part))

    # To run Depth Limited Search
    # NOTE: DLS only work properly on a perfect maze
    # m.tracePath({a: dlsvisited}, delay=10)
    # m.tracePath({b: dls_path}, delay=15)
    # l = textLabel(m, 'RUNNING DEPTH LIMITED SEARCH', '')
    # l3 = textLabel(m, 'Depth', DEPTH_LIMIT)
    # l1 = textLabel(m, 'Total cells explored', len(dlsvisited))
    # l2 = textLabel(m, 'Path length', len(dls_path))

    # To run Iterative Deepening Search
    # m.tracePath({a: idsvisited}, delay=15)
    # m.tracePath({b: ids_path}, delay=15)
    # l = textLabel(m, 'RUNNING DEPTH LIMITED SEARCH', '')
    # l3 = textLabel(m, 'Depth', DEPTH_LIMIT)
    # l1 = textLabel(m, 'Total cells explored', len(idsvisited))
    # l2 = textLabel(m, 'Path length', len(ids_path))

    m.run()


def main():
    menu()


if __name__ == '__main__':
    main()
