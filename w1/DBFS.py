from state import State


def dbfs(maze, fringe) -> bool:
    """Implements the DFS and BFS search algorithms

    Args:
        maze (Maze): A maze including all the paths
        fringe (Fringe): A Fringe, more specifically standart Queue

    Returns:
        bool: Whether or not a path was found
    """

    seen = set()
    room = maze.get_room(*maze.get_start())
    state = State(room, None, 0)
    fringe.push(state)
    seen.add(room)

    while not fringe.is_empty():
        state = fringe.pop()
        room = state.get_room()

        if room.is_goal():
            return resolve_goal_found(maze, fringe, state)

        for d in room.get_connections():
            new_room, cost = room.make_move(d, state.get_cost())
            if new_room not in seen:
                new_state = State(new_room, state, cost)
                fringe.push(new_state)
                seen.add(new_room)

    print("not solved")
    fringe.print_stats()
    return False


def resolve_goal_found(maze, fringe, state):
    """Prints the summary of the best path

    Args:
        maze (Maze): A maze including all the paths
        fringe (Fringe): Any Fringe
        state (State): The latest explored state

    Returns:
        bool: True
    """
    print("solved")
    fringe.print_stats()
    state.print_path()
    state.print_actions()
    print()
    maze.print_maze_with_path(state)
    return True
