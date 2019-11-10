def sqroot(goal=2, max_iterations=70):

    lower, upper = 1, goal
    last = upper

    if goal < 1:
        lower, upper = goal, 1

    for itt in range(max_iterations):
        attempt = (lower + upper) * 0.5

        if attempt == last or attempt * attempt == goal:
            return attempt, itt

        elif attempt * attempt < goal:
            lower = attempt

        else:
            upper = attempt

        last = attempt

    else:
        print("not found, try increasing max_iterations")

for n in range(1, 100):
    v = n/100
    answer, tries = sqroot(v)
    print(f"Square root of {v} is {answer} (took {tries} iterations)")
for n in range(1,10000):
    answer, tries = sqroot(n)
    print(f"Square root of {n} is {answer} (took {tries} iterations)")
