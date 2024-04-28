from fringe import Fringe
from state import State


def ids(maze):
    depth = 3
    while True:
        t, fringe, state = ds(maze, depth)
        if t is None:
            depth += 3

        elif t:
            print("solved")
            fringe.print_stats()
            state.print_path()
            state.print_actions()
            print()
            maze.print_maze_with_path(state)
            return

        else:
            print("not solved")
            fringe.print_stats()
            return


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
            return True, fringe, state

        for d in room.get_connections():
            new_room, cost = room.make_move(d, state.get_cost())
            if new_room not in seen:
                new_state = State(new_room, state, cost)
                fringe.push(new_state)
                seen.add(new_room)
        depth += 1

        if depth > max_depth:
            return None, None, None

    return False, fringe, state
