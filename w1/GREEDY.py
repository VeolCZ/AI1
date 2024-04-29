from DBFS import resolve_goal_found
from state import State


def greedy(maze, fringe) -> bool:
    """Implements the GREEDY search algorithm

    Args:
        maze (Maze): A maze including all the paths
        fringe (Fringe): A Fringe, more specifically standart Stack

    Returns:
        bool: Whether or not a path was found
    """

    seen = set()
    room = maze.get_room(*maze.get_start())
    state = State(room, None, 0 + room.heuristicValue)
    fringe.push(state)
    seen.add(room)

    while not fringe.is_empty():
        state = fringe.pop()
        room = state.get_room()
        neighbours = []

        if room.is_goal():
            return resolve_goal_found(maze, fringe, state)

        for c in room.get_connections():
            neighbours.append(room.make_move(c, state.get_cost()))
        neighbours.sort(key=lambda a: a[0].heuristicValue)

        for _ in range(len(neighbours)):
            new_room, cost = neighbours.pop()
            if new_room not in seen:
                fringe.push(State(new_room, state, cost + new_room.heuristicValue))
                seen.add(new_room)

    print("not solved")
    fringe.print_stats()
    return False
