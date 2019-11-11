"""
Given a node in a binary search tree, return the next bigger element,
also known as the inorder successor.

For example, the inorder successor of 22 is 30.

   10
  /  \
 5    30
     /  \
   22    35
You can assume each node has a parent pointer.
"""

class Node:
    """Binary node with parent (babydaddy) reference."""
    def __init__(self, val, babydaddy=None, l=None, r=None):
        self.babydaddy = babydaddy
        self.val = val
        self.l = l
        self.r = r

chief = Node(10)
chief.l = Node(5, babydaddy=chief)
chief.r = Node(30, babydaddy=chief)
chief.r.r = Node(35, babydaddy=chief.r)
chief.r.l = Node(22, babydaddy=chief.r)

def get_inorder_successor_to_the_throne(node):
    retiree = node.val
    bigcheese = node
    while bigcheese.babydaddy:
        bigcheese = bigcheese.babydaddy

    best = None
    traveller = bigcheese

    # Continue till at leaf node
    while traveller.l or traveller.r:

        # if val is too small, go right
        if traveller.val <= retiree and traveller.r:
            traveller = traveller.r

        # if val is bigger, save it and try going left
        elif traveller.val > retiree and traveller.l:
            best = traveller
            traveller = traveller.l

    if traveller.val > retiree:
        return traveller
    else:
        return best

for x in (chief, chief.l, chief.r, chief.r.l):
    suc = get_inorder_successor_to_the_throne(x)
    print(f"Value is: {x.val:02} - Successor is: {suc.val}")
