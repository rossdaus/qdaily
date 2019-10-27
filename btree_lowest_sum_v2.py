class Node:
    """Class to represent a node."""
    def __init__(self, val=None, l=None, r=None):
        self.val, self.l, self.r = val, l, r

    def level_sums(self, sums={}, level=0):
        """Find sum of each level. Returns dict."""
        if level not in sums:
            sums[level] = 0
        sums[level] += self.val

        if self.l:
            self.l.level_sums(sums, level + 1)
        if self.r:
            self.r.level_sums(sums, level + 1)

        return sums

    def min_level_sum(self):
        """Return level which has lowest sum."""
        sums = self.level_sums()
        lowest_sum = min(v for v in sums.values())
        return next(k for k, v in sums.items() if v == lowest_sum)

#                  10
#            8              2
#          3   4          2

tree = Node(10, Node(8, Node(3), Node(4)), Node(2, Node(2)))
answer = tree.min_level_sum()
print(answer)
