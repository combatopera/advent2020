from adventlib import inpath
from collections import defaultdict

class Node:

    def __init__(self):
        self.children = []

def main():
    tree = defaultdict(Node)
    for line in inpath().read_text().splitlines():
        x, y = line.split(')')
        tree[x].children.append(y)
    tree['COM'].orbits = 0
    keys = ['COM']
    while keys:
        nextkeys = []
        for x in keys:
            n0 = tree[x]
            for n1 in (tree[y] for y in n0.children):
                n1.orbits = n0.orbits + 1
            nextkeys.extend(n0.children)
        keys = nextkeys
    print(sum(n.orbits for n in tree.values()))
