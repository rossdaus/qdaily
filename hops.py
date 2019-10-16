def solve(a, pos=0, *path):
    """
    Find route to end of list a.
    pos is our current position (index of the array)
    path is a tuple of values containing our previous positions (indexes)
    """
    # If at end of array we are successful, return the path we took
    if pos == len(a) - 1:
        return (*path, pos)

    # get absolute of current hop value, fail if out of range
    try:
        hops = abs(a[pos])
    except IndexError:
        return False

    # Fail if landed on a 0, or have been at this position
    if hops == 0 or pos in path:
        return False

    # Solve for forward and backward hops
    return solve(a, pos + hops, *path, pos) or \
           solve(a, pos - hops, *path, pos)

goods = (
    [-2, 0, -1, 0],
    [3, 2, 1, 1],
    [2, -7, -2, -4, 3, 0, 0, 0, 9],
    [1, 2, -3, 1, 0, 2],
)

bads = (
    [1, 1, 0, 1],
    [6, 3, 2],
    [2, 6, 2, 3, 0, 1],
    [1, -3, 2, 0, 2, 0]
)

for x in goods + bads:
    answer = solve(x)
    print(answer)
