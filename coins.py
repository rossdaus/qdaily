import random

def generate_matrix(x, y):
    """Generate a random matrix of coins, size x * y."""
    matrix = list()

    for i in range(y):
        row = list()

        for j in range(x):
            row.append(random.choice(range(9)))

        matrix.append(row)
        print(row)

    return matrix


def get_route_sum(matrix, route, sums=dict()):
    """Total up money collected for a particular route."""
    if not route:
        return 0

    if route not in sums:
        x, y = 0, 0
        money = matrix[y][x]

        for direction in route:

            if direction == "R":
                x += 1
            else:
                y += 1

            money += matrix[y][x]

        print("calculating: " + route + ".   Money : " + str(money))
        sums[route] = money

    return sums[route]


def get_best(matrix, x=0, y=0, route="", bestroute=""):

    xmax, ymax = len(matrix[0]), len(matrix)
    # rsum = lambda r: get_route_sum(matrix, r)
    def rsum(r):
        return get_route_sum(matrix, r)

    # can we move right, can we move down?
    canright = True if x < xmax-1 else False
    candown = True if y < ymax-1 else False

    if canright and candown:
        bestroute = max((bestroute,
                        get_best(matrix, x+1, y, route+"R", bestroute),
                        get_best(matrix, x, y+1, route+"D", bestroute)
                        ), key=rsum)

    elif canright:
        bestroute = max((bestroute,
                        get_best(matrix, x+1, y, route+"R", bestroute)
                        ), key=rsum)
    elif candown:
        bestroute = max((bestroute,
                        get_best(matrix, x, y+1, route+"D", bestroute)
                        ), key=rsum)


    else:
        if rsum(route) > rsum(bestroute):
            bestroute = route

    return bestroute


def solve(matrix):
    bestroute = get_best(matrix)
    for line in matrix:
        print(line)
    print("bestroute :", ",".join(x for x in bestroute))
    print("money:", get_route_sum(matrix, bestroute))

m = generate_matrix(5,5)
solve(m)
