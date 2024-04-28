from state import State


def astar(maze, fringe):
    seen = set()
    room = maze.get_room(*maze.get_start())
    state = State(room, None)
    fringe.push(state)

    while not fringe.is_empty():
        state = fringe.pop()
        room = state.get_room()
        seen.add(room)
        cringe = []
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
            new_room, cost = room.make_move(d, state.get_cost())
            neighbours.append(hash(new_room))

        while not fringe.is_empty():
            _state = fringe.pop()
            cringe.append(_state)

        for _state in cringe:
            if hash(_state.get_room()) in neighbours:
                for d in room.get_connections():
                    new_cost = float("inf")
                    new_room, cost = room.make_move(d, state.get_cost())
                    if new_room == _state.get_room():
                        new_cost = cost + state.cost + new_room.heuristicValue
                        if new_cost < _state.cost:
                            _state.cost = new_cost
                        break
            fringe.push(_state)

        for d in room.get_connections():
            new_room, cost = room.make_move(d, state.get_cost())
            if new_room not in seen:
                new_state = State(new_room, state, cost + new_room.heuristicValue)
                fringe.push(new_state)
                seen.add(new_room)

    print("not solved")
    fringe.print_stats()
    return False
