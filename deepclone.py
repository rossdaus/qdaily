import random

class Node:
    """Class to define a node with next pointer and random pointer."""
    def __init__(self, val):
        self.val = val
        self.next = None
        self.rand = None

def deepclone(orig):
    """Deep clone the singly-linked list with random pointers."""

    # First clone the linked list without the random pointers

    # Create the cloned head node using the value of the original head
    clone = Node(orig.val)

    # Save a reference to head element of each list
    orighead = orig
    clonehead = clone

    # Create linked nodes in the clone using values of the original list
    while orig.next:
        clone.next = Node(orig.next.val)
        orig = orig.next
        clone = clone.next

    # Reassign clone and orig to point at their respective heads
    clone = clonehead
    orig = orighead

    # Now clone the random pointers
    while orig:  # iterate through nodes of orig
        rand = orig.rand # Get reference to random element

        # Search entire linked list for the random item, for this
        # we must start at the heads
        ocur = orighead
        ccur = clonehead

        # Skip over items that are not the random node we are looking for
        while rand is not ocur:
            ocur = ocur.next
            ccur = ccur.next

        # Found the referenced random node, set the clone to point to
        # it's corresponding random node
        clone.rand = ccur

        # Repeat the process for each node
        orig = orig.next
        clone = clone.next

    # Return the head of the cloned linked list
    return clonehead


"""Test the cloning"""

# Create four nodes
nodes = Node(1), Node(2), Node(3), Node(4)

# Set each node to point to the next node
for i in range(len(nodes) - 1): nodes[i].next = nodes[i + 1]

# Set each node to point to a random node
for n in nodes: n.rand = random.choice(nodes)

# Get reference to head node
orig = nodes[0]

# Create a deep clone using the head of the original linked list
clone = deepclone(orig)

while orig:
    print("Original values :", orig.val, orig.rand.val, end = "      ")
    print("Clone values    :", clone.val, clone.rand.val)

    # Ensure we are looking at separate objects with the same value
    assert orig.val == clone.val
    assert orig.rand.val == clone.rand.val
    assert orig is not clone
    assert orig.rand is not clone.rand
    if orig.next or clone.next:
        assert orig.next is not clone.next
        assert orig.next.rand is not clone.next.rand

    orig = orig.next
    clone = clone.next
