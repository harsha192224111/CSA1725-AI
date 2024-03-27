def valid(state):
    m1, c1, b, m2, c2 = state
    return (
            0 <= m1 <= 3
        and 0 <= c1 <= 3
        and 0 <= m2 <= 3
        and 0 <= c2 <= 3
        and (m1 == 0 or m1 >= c1)
        and (m2 == 0 or m2 >= c2)
    )

def gen_next_state(state):
    m1, c1, b, m2, c2 = state
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    nextstate = []
    for dm, dc in moves:
        if b == 1:
            newstate = (m1 - dm, c1 - dc, 0, m2 + dm, c2 + dc)
        else:
            newstate = (m1 + dm, c1 + dc, 1, m2 - dm, c2 - dc)
        if valid(newstate):
            nextstate.append(newstate)
    return nextstate

def bfs(start_state):
    queue = [(start_state, [start_state])]

    while queue:
        currstate, path = queue.pop(0)
        if currstate == (0, 0, 0, 3, 3):
            return path
        for next_state in gen_next_state(currstate):
            if next_state not in path:
                queue.append((next_state, path + [next_state]))
                print(queue)
    return None

start_state = (3, 3, 1, 0, 0)
solution = bfs(start_state)
if solution:
    for state in solution:
        m1, c1, b, m2, c2 = state
        print(
            f"{m1} missionaries, {c1} cannibals, {'boat on left' if b == 1 else 'boat on right'}, {m2} missionaries, {c2} cannibals"
        )
else:
    print("no solution")
