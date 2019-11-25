#!/usr/bin/env python3

class Node:
    """A Node with left and right children."""
    def __init__(self, val, l=None, r=None):
        self.val = val
        self.l = l
        self.r = r

    def __repr__(self):
        """Print tree as val[left,right] """
        out = ""

        if self is not None:
            out += str(self.val)

        if self.l or self.r:
            out += f"[{str(self.l) if self.l is not None else ''}" \
                f"{',' + str(self.r) if self.r is not None else ''}]"
        return out


def can_prune(node):
    """Return whether a node can be pruned."""

    # can prune None nodes (they are in effect already pruned)
    if node is None:
        return True

    # cannot prune nodes with value 1
    if node.val is 1:
        return False

    # can prune nodes with value 0 only if all descendants are prunable.
    if node.val is 0:
        return can_prune(node.l) and can_prune(node.r)

def prune(node):
    """Perform pruning by first checking whether each node is prunable."""
    if node is None:
        return  # do nothing

    if can_prune(node.l):
        node.l = None  # To prune just set the value to None

    if can_prune(node.r):
        node.r = None  # To prune just set the value to None

    prune(node.l)  # repeat recursively for descendants.
    prune(node.r)


tree = Node(0, Node(1), Node(0, Node(1, Node(0), Node(0)), Node(0)))

print(tree)
prune(tree)
print(tree)

# Output:
# 0[1,0[1[0,0],0]]
# 0[1,0[1]]
