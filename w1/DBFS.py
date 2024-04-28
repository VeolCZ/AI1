from state import State


def dbfs(maze, fringe):
    seen = set()
    room = maze.get_room(*maze.get_start())
    state = State(room, None)
    fringe.push(state)

    while not fringe.is_empty():
        state = fringe.pop()
        room = state.get_room()
        seen.add(room)

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
            if new_room not in seen:
                new_state = State(new_room, state, cost)
                fringe.push(new_state)
                seen.add(new_room)

    print("not solved")
    fringe.print_stats()
    return False