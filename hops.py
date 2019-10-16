def solve(a, pos=0, *path):
    """
    Find route to end of list a.
    pos is our current position (index of the array)
    path is a tuple of values containing our previous positions
    """
    # If at end of array we are successful, return the path we took
    if pos == len(a) - 1:
        return (*path, pos)

    # Quit on repetition, out of range or hop value of 0
    if pos in path or pos < 0 or pos + 1 > len(a) or a[pos] == 0:
        return False

    # Solve for forward and backward hops
    hops = abs(a[pos])
    return solve(a, pos + hops, *path, pos) or solve(a, pos - hops, *path, pos)

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
