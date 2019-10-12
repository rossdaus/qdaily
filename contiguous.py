def solve(l, k):
    for n in range(len(l)):
        total = 0
        elements = l[n:]
        count = 0
        for x in elements:
            if total == k:
                return elements[:count]
            elif total > k:
                break
            total += x
            count += 1

l = [4, 6, 3, 6, 20, 30, 40, 5, 3, 2, 64, 34]
k = 100
answer = solve(l, k)
print(answer)


