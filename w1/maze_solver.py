#!/usr/bin/env python3
from fringe import Fringe
from state import State


def solve_maze_general(maze, algorithm):
    """
    Finds a path in a given maze with the given algorithm
    :param maze: The maze to solve
    :param algorithm: The desired algorithm to use
    :return: True if solution is found, False otherwise
    """
    # select the right fringe for each algorithm
    if algorithm == "BFS":
        fringe = Fringe("FIFO")
    elif algorithm == "DFS":
        fringe = Fringe("STACK")
    elif algorithm == "UCS":
        fringe = Fringe("PRIORITY")
    else:
        print("Algorithm not found/implemented, exit")
        return

    # get the start room, create state with start room and None as parent and put it in fringe
    room = maze.get_room(*maze.get_start())
    state = State(room, None)
    fringe.push(state)
    seen = set()

    while not fringe.is_empty():

        # get item from fringe and get the room from that state
        state = fringe.pop()
        room = state.get_room()
        seen.add(room)

        if algorithm == "UCS":
            cringe = []
            neighbours: list[int] = []
            for d in room.get_connections():
                new_room, cost = room.make_move(d, state.get_cost())
                neighbours.append(hash(new_room))

            # new_fringe = Fringe("PRIORITY")
            while not fringe.is_empty():
                _state = fringe.pop()
                cringe.append(_state)

            for _state in cringe:

                if hash(_state.get_room()) in neighbours:
                    for d in room.get_connections():
                        new_cost = float("inf")
                        new_room, cost = room.make_move(d, state.get_cost())
                        if new_room == _state.get_room():
                            new_cost = cost + state.cost
                            if new_cost < _state.cost:
                                _state.cost = new_cost
                            break

                fringe.push(_state)

        if room.is_goal():
            # if room is the goal, print that with the statistics and the path and return
            print("solved")
            fringe.print_stats()
            state.print_path()
            state.print_actions()
            print()  # print newline
            maze.print_maze_with_path(state)
            return True

        for d in room.get_connections():
            # loop through every possible move
            new_room, cost = room.make_move(
                d, state.get_cost()
            )  # Get new room after move and cost to get there
            if new_room not in seen:
                new_state = State(
                    new_room, state, cost
                )  # Create new state with new room and old room
                fringe.push(new_state)  # push the new state
                seen.add(new_room)

    print("not solved")  # fringe is empty and goal is not found, so maze is not solved
    fringe.print_stats()  # print the statistics of the fringe
    return False
