import random

def prob_selector(i, p):
    """Return element from i with probability of its index in p."""
    r = random.random() # random float between 0 and 1

    for x in range(len(p)):
        r = r - p[x]

        if r <= 0:
            return i[x]

# TEST
def test(i, p, runs=100 * 1000):
    """Test with 100,000 runs."""

    d = dict.fromkeys(i, 0)

    for x in range(runs):
        answer = prob_selector(i, p)
        d[answer] += 1

    return {k: f'{d[k] / runs:.3f}' for k in d}


i = 1, 2, 3, 4
p = 0.1, 0.5, 0.2, 0.2
print(p)
for _ in range(6):
    print(test(i, p))
