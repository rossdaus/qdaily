import random
D = "0"
R = "1"

def generate_matrix(x, y):
    """Generate a random matrix of coins, size x * y."""
    matrix = list()

    for i in range(y):
        row = list()

        for j in range(x):
            row.append(random.choice(range(9)))

        matrix.append(row)

    return matrix


def get_route_sum(matrix, route, sums=dict()):
    """Total up money collected for a particular route."""
    if not route:
        return 0

    if route not in sums:
        x, y = 0, 0
        money = matrix[y][x]

        for direction in route:

            if direction == R:
                x += 1
            else:
                y += 1

            money += matrix[y][x]

        # print("calculating: " + route + "   Money : " + str(money))
        sums[route] = money

    return sums[route]


def get_best(matrix, route="", bestroute=""):

    x, y = route.count(R), route.count(D)
    xmax, ymax = len(matrix[0]), len(matrix)
    def rsum(r): return get_route_sum(matrix, r)

    # can we move right, can we move down?
    canright = True if x < xmax-1 else False
    candown = True if y < ymax-1 else False

    if canright and candown:
        bestroute = max((bestroute,
                        get_best(matrix, route + R, bestroute),
                        get_best(matrix, route + D, bestroute)
                        ), key=rsum)

    elif canright:
        bestroute = max((bestroute,
                         get_best(matrix, route + R, bestroute)), key=rsum)
    elif candown:
        bestroute = max((bestroute,
                        get_best(matrix, route + D, bestroute)), key=rsum)


    else:
        if rsum(route) > rsum(bestroute):
            bestroute = route

    return bestroute


def solve(matrix):
    bestroute = get_best(matrix)
    print()
    for line in matrix:
        print(line)
    print("bestroute :", ",".join(x for x in bestroute))
    print("money:", get_route_sum(matrix, bestroute))

m = generate_matrix(3,3)
solve(m)
