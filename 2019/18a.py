from adventlib import inpath, Vector
from functools import partial
from string import ascii_lowercase, ascii_uppercase
import networkx as nx

acceptdoors = set(ascii_uppercase)
acceptnodes = {'@', *ascii_lowercase}
doormasks = {c: 1 << (ord(c) - ord('A')) for c in ascii_uppercase}
keymasks = {c: 1 << (ord(c) - ord('a')) for c in ascii_lowercase}
moves = [(x, y) for r in [range(-1, 2)] for x in r for y in r if abs(x) ^ abs(y)]

def bfs(*objs, cullkey = None):
    def deco(objs, proc):
        if cullkey is None:
            unseen = lambda o: True
        else:
            seen = set()
            def unseen(o):
                if o not in seen:
                    seen.add(o)
                    return True
        while objs:
            nextobjs = []
            for obj in objs:
                if unseen(obj):
                    nextobjs.extend(proc(obj))
            objs = nextobjs
    return partial(deco, objs)

class Edge:

    @classmethod
    def seed(cls, c, p):
        return cls(c, c, 0, 0, p)

    @classmethod
    def _of(cls, *args):
        return cls(*args)

    def __init__(self, start, end, requires, weight, tip):
        self.start = start
        self.end = end
        self.requires = requires
        self.weight = weight
        self.tip = tip

    def popsteps(self, grid):
        for m in moves:
            q = self.tip + m
            if q in grid:
                c = grid.pop(q)
                yield self._of(self.start, c, self.requires | doormasks.get(c, 0), self.weight + 1, q)

def _mainimpl(block):
    grid = {}
    for y, line in enumerate(block.splitlines()):
        for x, c in enumerate(line):
            p = Vector([x, y])
            if '@' == c:
                origin = p
            elif '#' != c:
                grid[p] = c
    G = nx.Graph()
    @bfs(Edge.seed('@', origin))
    def proc(e):
        for f in e.popsteps(grid):
            if f.end in acceptnodes:
                G.add_edge(f.start, f.end, requires = f.requires, weight = f.weight)
                yield Edge.seed(f.end, f.tip)
            else:
                yield f
    print(G)
    print(nx.get_edge_attributes(G, 'requires'))
    print(nx.get_edge_attributes(G, 'weight'))
    maxkeys = (1 << (len(G) - 1)) - 1
    print(maxkeys)
    H = nx.DiGraph()
    @bfs(('@', 0), cullkey = lambda x: x)
    def proc(n):
        c, keys = n
        for e in G.edges(c, True):
            if keys | e[2]['requires'] == keys:
                dest = e[1], keys | keymasks.get(e[1], 0)
                H.add_edge(n, dest, weight = e[2]['weight'])
                if dest[1] != maxkeys:
                    yield dest
    print(H)
    print(nx.get_edge_attributes(H, 'weight'))

def main():
    for block in inpath().read_text().split('\n\n'):
        _mainimpl(block)
