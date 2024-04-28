from fringe import Fringe
from state import State


def ids(maze):
    depth = 3
    while True:
        res = ds(maze, depth)
        if res is not None and res is not False:
            fringe, state = res
            print("solved")
            fringe.print_stats()
            state.print_path()
            state.print_actions()
            print()
            maze.print_maze_with_path(state)
            return

        if res is False:
            print("not solved")
            fringe.print_stats()
            return

        depth += 3


def ds(maze, max_depth):
    fringe = Fringe("STACK")
    depth = 0
    seen = set()
    room = maze.get_room(*maze.get_start())
    state = State(room, None)
    fringe.push(state)

    while not fringe.is_empty():
        state = fringe.pop()
        room = state.get_room()
        seen.add(room)

        if room.is_goal():
            return fringe, state

        for d in room.get_connections():
            new_room, cost = room.make_move(d, state.get_cost())
            if new_room not in seen:
                new_state = State(new_room, state, cost)
                fringe.push(new_state)
                seen.add(new_room)
        depth += 1

        if depth > max_depth:
            return None

    return False
