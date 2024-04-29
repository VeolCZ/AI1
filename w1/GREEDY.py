from DBFS import resolve_goal_found
from state import State


def greedy(maze, fringe):
    seen = set()
    room = maze.get_room(*maze.get_start())
    state = State(room, None)
    fringe.push(state)

    while not fringe.is_empty():
        state = fringe.pop()
        room = state.get_room()
        seen.add(room)
        neighbours: list[int] = []

        if room.is_goal():
            return resolve_goal_found(maze, fringe, state)

        for d in room.get_connections():
            neighbours.append(room.make_move(d, state.get_cost()))
        neighbours.sort(key=lambda a: a[0].heuristicValue)

        for _ in range(len(neighbours)):
            new_room, cost = neighbours.pop()
            if new_room not in seen:
                fringe.push(State(new_room, state, cost))
                seen.add(new_room)

    print("not solved")
    fringe.print_stats()
    return False
