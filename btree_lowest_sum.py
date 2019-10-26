class Node:
    """Class to represent a node."""
    def __init__(self, val=None, l=None, r=None):
        self.val, self.l, self.r = val, l, r

    def __repr__(self):
        """Define output of print function."""
        if self.l or self.r:
            return (f"{self.val}[{self.l if self.l else ''},"
                    f"{self.r if self.r else ''}]")
        return str(self.val)


def level_with_min_sum(root):
    """Find level of tree with the lowest sum."""
    sums, level, digits = {}, 0, ""
    for char in str(tree):  # loop over characters in tree representation
        if char.isdigit():  # collect digit characters
            digits += char
            continue
        elif digits:  #  add digits to whatever level we are on
            sums[level] = 0 if level not in sums else sums[level]
            sums[level] += int(digits)
            if char in "[]":  # increment or decrement current level
                level += (1 if char == "[" else -1)
        digits = ""

    lowest = min(v for k, v in sums.items())
    return  next(k for k, v in sums.items() if v == lowest)

#                  10
#            8              2
#          3   4          2

tree = Node(10, Node(8, Node(3), Node(4)), Node(2, Node(2)))
# 10[8[3,4],2[2,]]

answer = level_with_min_sum(tree)
print(f"level of tree with lowest sum is level: {answer}")
