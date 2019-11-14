#!/usr/bin/env python3
class Node:
    """Binary node."""
    def __init__(self, val, l=None, r=None):
        self.val, self.l, self.r = val, l, r


def mps(node, total=0, path=[]):
    """Return minimum path sum and path taken."""

    # Node with no children (leaf)
    if not node.l and not node.r:
        return total + node.val, path + [node.val]

    # One child
    if node.l and not node.r:
        return mps(node.l, total + node.val, path + [node.val])

    if node.r and not node.l:
        return mps(node.r, total + node.val, path + [node.val])

    # Two children
    return min(mps(node.l, total + node.val, path + [node.val]),
               mps(node.r, total + node.val, path + [node.val]))

#          10
#      5        5
#        2        1
#              -1

tree = Node(10, Node(5, None, Node(2)), Node(5, None, Node(1, Node(-1))))
print(mps(tree))
#output: (15, [10, 5, 1, -1])
