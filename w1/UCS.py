from DBFS import resolve_goal_found
from state import State


def ucs(maze, fringe) -> bool:
    """Implements the A* search algorithm

    Args:
        maze (Maze): A maze including all the paths
        fringe (Fringe): A Fringe, more specifically heap

    Returns:
        bool: Whether or not a path was found
    """

    room = maze.get_room(*maze.get_start())
    state = State(room, None, 0)
    fringe.push(state)
    seen = dict()
    seen[room] = state

    while not fringe.is_empty():
        state = fringe.pop()
        room = state.get_room()

        if room.is_goal():
            return resolve_goal_found(maze, fringe, state)

        for c in room.get_connections():
            new_room, cost = room.make_move(c, state.get_cost())
            if new_room not in seen:
                new_state = State(
                    new_room,
                    state,
                    cost,
                    priority=cost,
                )
                fringe.push(new_state)
                seen[new_room] = new_state
            else:
                new_cost = cost + state.get_cost()
                if new_cost < seen[new_room].get_cost():
                    seen[new_room] = State(
                        new_room,
                        state,
                        new_cost,
                        priority=new_cost,
                    )

    print("not solved")
    fringe.print_stats()
    return False
