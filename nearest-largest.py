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
    table = [nearest(arr, n) for n in range(len(arr))]

    for n in range(len(arr)):
        arr[n] = table[n]

def fast_nearest(preprocessed_arr, idx):
    """Pre processed solution."""
    return preprocessed_arr[idx]


arr = list(range(25))
random.shuffle(arr)
print(arr)

for index in range(6):
    answer = nearest(arr, index)
    print(f"Nearest to index {index} is index {answer}")

# pre-process array
print("\nPre-processed method:\n")
pre_process(arr)
for index in range(6):
    answer = fast_nearest(arr, index)
    print(f"Nearest to index {index} is index {answer}")
