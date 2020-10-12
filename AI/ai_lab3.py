# Bredth first search in search of target - Using Brute Force Algorithms

def bfs(src, target, visited_states):
    # Use brute force technique
    que=[]
    que.append(src)
    if src == target:
        return True
    while True:
        visited_states.append(src)
        adj = possible_moves(src, visited_states)
        for i in adj:
            que.append(i)

        for move in que:
            if move == target:
                print(move)
                return True

        if que:
            que.pop(0)
            if que:
                src=que[0]
            else:
                return False


def possible_moves(state, visited_states):
    b = state.index(-1)

    # 'd' for down, 'u' for up, 'r' for right, 'l' for left - directions array
    d = []

    # Add all possible direction into directions array - Hint using if statements
    if b <= 5:
        d.append('d')

    if b >= 3:
        d.append('u')

    if b % 3 < 2:
        d.append('r')

    if b % 3 > 0:
        d.append('l')

    # If direction is possible then add state to move
    pos_moves = []

    # for all possible directions find the state if that move is played
    ### Jump to gen function to generate all possible moves in the given directions
    for i in d:
        temp = gen(state, i, b)
        # return all possible moves only if the move not in visited_states
        if temp not in visited_states:
            pos_moves.append(temp)

    return pos_moves


def gen(state, m, b):  # m(move) is direction to slide, b(blank) is index of empty spot
    # create a copy of current state to test the move

    temp = state.copy()

    # if move is to slide empty spot to the left and so on
    if m == "l":
        temp[b], temp[b - 1] = temp[b - 1], temp[b]
    if m == "r":
        temp[b], temp[b + 1] = temp[b + 1], temp[b]
    if m == "d":
        temp[b], temp[b + 3] = temp[b + 3], temp[b]
    if m == "u":
        temp[b], temp[b - 3] = temp[b - 3], temp[b]

    # return new state with tested move to later check if "src == target"
    return temp


src = [1, 2, 3, -1, 4, 5, 6, 7, 8]
target = [2, -1, 3, 1, 4, 5, 6, 7, 8]
visited_states = []

print(bfs(src, target, visited_states))
