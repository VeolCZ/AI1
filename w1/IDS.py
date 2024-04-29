from DBFS import resolve_goal_found
from fringe import Fringe
from state import State


def ids(maze) -> bool:
    """Implements the itterative deepening search algorithm

    Args:
        maze (Maze): A maze including all the paths

    Returns:
        bool: Whether or not a path was found
    """

    depth = 3
    while True:
        t, fringe, state = ds(maze, depth)
        if t is None:
            depth += 3

        elif t:
            return resolve_goal_found(maze, fringe, state)

        else:
            print("not solved")
            fringe.print_stats()
            return False


def ds(maze, max_depth):
    """Inner function fo IDS search algorithm

    Args:
        maze (Maze): A maze including all the paths
        max_depth(int): Max depth to explore

    Returns:
        bool: Whether or not a path was found
    """

    fringe = Fringe("STACK")
    depth = 0
    seen = set()
    room = maze.get_room(*maze.get_start())
    state = State(room, None, 0 + room.heuristicValue)
    fringe.push(state)
    seen.add(room)

    while not fringe.is_empty():
        state = fringe.pop()
        room = state.get_room()

        if room.is_goal():
            return True, fringe, state

        for d in room.get_connections():
            new_room, cost = room.make_move(d, state.get_cost())
            if new_room not in seen:
                new_state = State(new_room, state, cost + new_room.heuristicValue)
                fringe.push(new_state)
                seen.add(new_room)
        depth += 1

        if depth > max_depth:
            return None, None, None

    return False, fringe, state
