from adventlib import inpath, Vector
from functools import partial
from string import ascii_lowercase, ascii_uppercase
import networkx as nx

acceptdoors = set(ascii_uppercase)
acceptnodes = {'@', *ascii_lowercase}
doormasks = {c: 1 << (ord(c) - ord('A')) for c in ascii_uppercase}
moves = [(x, y) for r in [range(-1, 2)] for x in r for y in r if abs(x) ^ abs(y)]

def bfs(*objs):
    def deco(objs, proc):
        while objs:
            nextobjs = []
            for obj in objs:
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

    def __init__(self, start, end, doors, weight, tip):
        self.start = start
        self.end = end
        self.doors = doors
        self.weight = weight
        self.tip = tip

    def popsteps(self, grid):
        for m in moves:
            q = self.tip + m
            if q in grid:
                c = grid.pop(q)
                yield self._of(self.start, c, self.doors | doormasks.get(c, 0), self.weight + 1, q)

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
                G.add_edge(f.start, f.end, doors = f.doors, weight = f.weight)
                yield Edge.seed(f.end, f.tip)
            else:
                yield f
    print(G)
    print(nx.get_edge_attributes(G, 'doors'))
    print(nx.get_edge_attributes(G, 'weight'))
    return
    H = nx.DiGraph()
    @bfs(('@', 0))
    def proc(n):
        c, keys = n
        for e in G.edges(c, True):
            print((c, keys | e[2]['requires']), e[1], e[2]['weight'])
        return
        yield

def main():
    for block in inpath().read_text().split('\n\n'):
        _mainimpl(block)
