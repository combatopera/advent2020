from adventlib import inpath
from collections import defaultdict

def main():
    tree = {}
    for line in inpath().read_text().splitlines():
        x, y = line.split(')')
        tree[y] = x
    sanancestors = {}
    k = 'SAN'
    n = 0
    while k in tree:
        k = tree[k]
        sanancestors[k] = n
        n += 1
    k = 'YOU'
    n = 0
    while k in tree:
        k = tree[k]
        if k in sanancestors:
            print(n + sanancestors[k])
            break
        n += 1
