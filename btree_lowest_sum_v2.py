class Node:
    """Class to represent a node."""
    def __init__(self, val=None, l=None, r=None):
        self.val, self.l, self.r = val, l, r

    def minlev(self, sums={}, level=0):
        """Find level which has the lowest sum."""
        sums[level] = sums.get(level, 0) + self.val

        if self.l:
            self.l.minlev(sums, level + 1)
        if self.r:
            self.r.minlev(sums, level + 1)

        return min(sums, key=sums.get)

#                  10
#            8              2
#          3   4          2

tree = Node(10, Node(8, Node(3), Node(4)), Node(2, Node(2)))
answer = tree.minlev()
print(answer)
