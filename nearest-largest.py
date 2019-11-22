import random

def nearest(arr, idx):
    """Simple Solution."""
    up = down = idx

    while up < len(arr) or down > -1:
        up += 1
        down -= 1

        if up < len(arr):
            if arr[idx] < arr[up]:
                return up

        if down > -1:
            if arr[idx] < arr[down]:
                return down


def pre_process(arr):
    """Create lookup table with all the answers."""
    table = [0] * len(arr)

    for n in range(len(arr)):
        table[n] = nearest(arr, n)

    for n in range(len(arr)):
        arr[n] = table[n]

def fast_nearest(preprocessed_arr, idx):
    """Pre processed solution."""
    return preprocessed_arr[idx]


arr = list(range(9))
random.shuffle(arr)
index = 3
print(arr)
answer = nearest(arr, index)
print(f"Nearest to index {index} is index {answer}")

# pre-process array
pre_process(arr)
answer = fast_nearest(arr, index)
print(f"Nearest to index {index} is index {answer}")
