def solve(l, k):
    for n in range(len(l)):
        total =  0
        for x in range(len(l[n:]) + 1):
            if total == k:
                return l[n:n + x]
            elif total > k:
                break
            total += l[n:][x]

l = [4, 6, 3, 6, 20, 30, 40, 5, 3, 2, 64, 34]
k = 100
answer = solve(l, k)
print(answer)
