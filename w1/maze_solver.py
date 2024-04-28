#!/usr/bin/env python3
from GREEDY import greedy
from fringe import Fringe
from DBFS import dbfs
from UCS import ucs


def solve_maze_general(maze, algorithm):
    """
    Finds a path in a given maze with the given algorithm
    :param maze: The maze to solve
    :param algorithm: The desired algorithm to use
    :return: True if solution is found, False otherwise
    """
    # select the right fringe for each algorithm
    if algorithm == "BFS":
        dbfs(maze, Fringe("FIFO"))
    elif algorithm == "DFS":
        dbfs(maze, Fringe("STACK"))
    elif algorithm == "UCS":
        ucs(maze, Fringe("PRIORITY"))
    elif algorithm == "GREEDY":
        greedy(maze, Fringe("STACK"))
    else:
        print("Algorithm not found/implemented, exit")
        return
