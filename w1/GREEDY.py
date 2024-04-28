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
            print("solved")
            fringe.print_stats()
            state.print_path()
            state.print_actions()
            print()
            maze.print_maze_with_path(state)
            return True

        for d in room.get_connections():
            neighbours.append(room.make_move(d, state.get_cost()))

        neighbours.sort(key=lambda a: a[0].heuristicValue)
        for _ in range(len(neighbours)):
            new_room, cost = neighbours.pop()
            neighbour = State(new_room, state, cost + new_room.heuristicValue)
            if neighbour not in seen:
                fringe.push(neighbour)
                seen.add(new_room)

    print("not solved")
    fringe.print_stats()
    return False
