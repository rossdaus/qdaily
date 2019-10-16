def solve(a, pos=0, *path):
    """
    Find route to end of list a.
    pos is our current position (index of the array)
    path is a tuple of values containing our previous positions (indexes)
    """

    # If at end of array we are successfull, return the path we took
    if pos == len(a) - 1:
        return (*path, pos)

    # get absolute of current hop value
    hops = abs(a[pos])

    # if we land on a 0 we have failed
    if hops == 0:
        return False

    # Assume we can go either back or forward
    back = forward = True

    # we cant go back if we have been there before or it is not in range
    if pos - hops < 0 or (pos - hops) in path:
        back = False

    # we cant go forward if we have been there before or it is not in range
    if pos + hops >= len(a) or (pos + hops) in path:
        forward = False

    # Fail if cant go forward or back
    if not forward and not back:
        return False

    # We can go forward or back so add current position to our path
    else:
        path = (*path, pos)

    # Solve for next hop
    if forward and not back:
        return solve(a, pos + hops, *path)
    elif back and not forward:
        return solve(a, pos - hops, *path)
    elif forward and back:
        return solve(a, pos + hops, *path) or solve(a, pos - hops, *path)

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
