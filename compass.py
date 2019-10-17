#!/usr/bin/env python3

north, east = {}, {}

def inferences(x, y, dimension, dirname):
    """Check each point in dict and add derived rules."""
    for point in dimension:
        if x in dimension[point] and point != y:
            print(f"Derived that {point} is {dirname} of {y}")
            add_rule(point, y, dimension)
    if y in dimension:
        for point in dimension[y]:
            if not point == x:
                print(f"Derived that {x} is {dirname} of {point}")
                add_rule(x, point, dimension)


def add_rule(x, y, dimension):
    """Add a rule to the dict of rules."""
    if x in dimension:
        dimension[x].add(y)
    else:
        dimension[x] = set(y)

def validate_rule(x, y, dimension):
    if dimension and y in dimension:
        return x not in dimension[y]
    return True

def parse(rulestring):
    """Turn a rule string into a list of rules."""
    r = rulestring.strip().split("\n")
    allrules = []
    for rule in r:
        x, directions, y = rule.split()
        for d in list(directions):
            allrules.append((x, y, d))
    return allrules


def solve(rules):
    parsed = parse(rules)
    for x, y, direction in parsed:
        flipped = True if direction in ("SW") else False
        dimension = north if direction in ("SN") else east
        dirname = "North" if direction in ("SN") else "East"
        if flipped:
            x, y = y, x
        add_rule(x, y, dimension)
        inferences(x, y, dimension, dirname)
        if not validate_rule(x, y, dimension):
            print(f"{x} cannot be {dirname} of {y} because {y} is {dirname} of {x}")
            return False
    return True

RULES = """
A NE B
C SW B
C NE D
E SW D
F N A
F SE G
"""
answer = solve(RULES)
print(answer)
