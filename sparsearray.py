class SparseArray:
    """A Sparse Array."""
    def __init__(me, arr, size=None):
        """Create dict of (index, value) for values that are not zero."""
        me.size = size or len(arr)
        me.data = {idx: val for idx, val in enumerate(arr) if val is not 0}

    def set(me, i, val):
        """Set a value."""
        if i > me.size:
            raise IndexError

        me.data[i] = val

    def get(me, i):
        """Get a value."""
        if not 0 <= i < me.size:
            raise IndexError

        return me.data.get(i, 0) # returns 0 if key not in dict

arr = [0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 7] + 200 * [0]
sparse = SparseArray(arr, len(arr))
sparse.set(214, 3)  # Update value at index 214 to 3
print(f"internal data    : {sparse.data}")
print(f"effective values : {[sparse.get(x) for x in range(len(arr))]}")
