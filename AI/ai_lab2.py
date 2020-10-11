def dfs(src, target, limit, visited_states):
    # Base case if Target found
    if src == target:
        return True

    # Base case if limit exceeded
    if limit <= 0:
        return False

    # Add source to visited_states
    visited_states.append(src)

    # Find possible slides up, down, left right to current empty site
    ### Jump to possible_moves function
    adj = possible_moves(src, visited_states)

    # For all possible moves gotten from the possible moves function
    # Check if src equals to new targets
    # Return True if target found in given depth limit
    for move in adj:
        if dfs(move, target, limit - 1, visited_states):
            return True
    return False


def possible_moves(state, visited_states):
    # Find index of empty spot and assign it to b
    for i, j in enumerate(src):
        if j == -1:
            b = i
            break

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


def iddfs(src, target, depth):
    visited_states = []

    for limit in range(1, depth+1):
        if dfs(src, target, limit, visited_states):
            return limit

    # Return Min depth at which the target was found
    return False


src = [1, 2, 3, -1, 4, 5, 6, 7, 8]
target = [1, 2, 3, 6, 4, 5, -1, 7, 8]

depth = 5

print("minimum depth target was found is:" + str(iddfs(src, target, depth)))  # Minimum depth should be 2