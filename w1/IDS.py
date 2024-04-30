from DBFS import resolve_goal_found
from state import State


def ids(maze, fringe) -> bool:
    """Implements the itterative deepening search algorithm

    Args:
        maze (Maze): A maze including all the paths
        fringe (Fringe): A fringe to use (a stack)

    Returns:
        bool: Whether or not a path was found
    """

    depth = 3
    states_visited = 0
    start = maze.get_room(*maze.get_start())
    while True:
        state, new_states_visited = ds(start, depth, fringe)

        if new_states_visited == -1:
            return resolve_goal_found(maze, fringe, state)

        if states_visited == new_states_visited:
            print("not solved")
            fringe.print_stats()
            return False

        depth += 3
        states_visited = new_states_visited


def ds(maze_start, max_depth, fringe):
    """Inner function fo IDS search algorithm

    Args:
        maze_start (Room): Starting point of the mazes
        max_depth (int): A max depth to which to explore
        fringe (Fringe): A fringe to use (a stack)

    Returns:
        bool: Whether or not a path was found
    """

    steps = 0
    state = State(maze_start, None)
    fringe.push(state)
    seen = set()
    seen.add(maze_start)

    while not fringe.is_empty():
        state = fringe.pop()
        steps += 1
        room = state.get_room()

        if room.is_goal():
            return state, -1

        if state.depth < max_depth:
            for d in room.get_connections():
                new_room, cost = room.make_move(d, state.get_cost())
                if new_room not in seen:
                    new_state = State(new_room, state, cost, depth=state.depth + 1)
                    fringe.push(new_state)
                    seen.add(new_room)

    return state, steps
