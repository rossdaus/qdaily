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
    if pos in path or not 0 <= pos < len(a) or a[pos] == 0:
        return False

    # Solve for next hops
    hops = a[pos]
    return solve(a, pos + hops, *path, pos)

goods = (
    [2, 2, -1, 0],
    [3, -9, -9, 1],
    [2, 8, 2, -4, -3, 0, 0, 0, 0, 9],
    [1, 2, 3, 2, 0, -3],
    [6, 4, 2, 4, -1, -3, -5, -6]
)

bads = (
    [1, -1, 1, 1],
    [3, 3, 2],
    [2, 6, 2, 3, -1, 1],
    [1, 3, 2, 0, -2, 0]
)

for x in goods + bads:
    answer = solve(x)
    print(answer)
