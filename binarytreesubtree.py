class Node:
    """Class to represent a node."""
    def __init__(self, val=None, l=None, r=None):
        self.val = val
        self.l = l
        self.r = r

    def __repr__(self):
        """Define output of print function."""
        if self.l or self.r:
            return f"{self.val}[{self.l},{self.r}]"
        return self.val

    def contains(self, other):
        """Determine if other is a subree of self."""
        if isinstance(other, Node):
            other = other.__repr__()
        if self.__repr__() == other:
            return True
        elif self.r and self.r.contains(other):
            return True
        elif self.l and self.l.contains(other):
            return True
        else:
            return False

def contains(atree, btree):
    """Does atree contain btree?"""
    print(atree)
    print(btree)
    print(atree.contains(btree), "\n")

first = Node("a")
first.l = Node("b", Node("d"), Node("e", Node("h"), Node("i")))
first.r = Node("c", Node("f"), Node("g"))

#            a[b[d,e[h,i]],c[f,g]]

#                    a
#                b       c
#              d   e    f g
#                 h i


second = Node("e", Node("x"), Node("i"))  # e[x,i]
contains(first, second)
# False

second.l = Node("h")  # e[h,i]
contains(first, second)
# True

third = Node("b", Node("d"), Node("e"))  #  b[d,e]
contains(first, third)
# False

third.r.l = Node("h")
third.r.r = Node("i")  #  b[d,e[h,i]]
contains(first, third)
# True
