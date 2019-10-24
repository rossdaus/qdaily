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

first = Node("a")
first.l = Node("b")
first.l.l = Node("d")
first.l.r = Node("e")
first.l.r.l = Node("h")
first.l.r.r = Node("i")
first.r = Node("c")
first.r.l = Node("f")
first.r.r = Node("g")

second = Node("e")
second.l = Node("x")
second.r = Node("i")

print(first)
print(second)
print(first.contains(second), "\n")
# False

second.l = Node("h")
print(first)
print(second)
print(first.contains(second), "\n")
# True

second = Node("b")
second.l = Node("d")
second.r = Node("e")
print(first)
print(second)
print(first.contains(second), "\n")
# False

second.r.l = Node("h")
second.r.r = Node("i")
print(first)
print(second)
print(first.contains(second), "\n")
# True
