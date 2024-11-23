from adventlib import inpath, Vector
from collections import namedtuple
from functools import partial
from string import ascii_lowercase, ascii_uppercase
import networkx as nx

acceptdoors = set(ascii_uppercase)
acceptrealnodes = {'@', *ascii_lowercase}
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

class Edge(namedtuple('BaseEdge', 'start end requires weight tip')):

    @classmethod
    def seed(cls, c, p):
        return cls(c, c, 0, 0, p)

    def popsteps(self, grid):
        for m in moves:
            q = self.tip + m
            if q in grid:
                c = grid.pop(q)
                yield self._make([self.start, c, self.requires | doormasks.get(c, 0), self.weight + 1, q])

def _mainimpl(block):
    grid = {}
    for y, line in enumerate(block.splitlines()):
        for x, c in enumerate(line):
            p = Vector([x, y])
            if '@' == c:
                origin = p
            elif '#' != c:
                grid[p] = c
    def intersections():
        for p, c in grid.items():
            if '.' == c and sum(1 for m in moves if p + m in grid) > 2:
                name = ','.join(map(str, p))
                grid[p] = name
                yield name
    intersections = set(intersections())
    G = nx.Graph()
    @bfs(Edge.seed('@', origin))
    def proc(e):
        for f in e.popsteps(grid):
            if f.end in acceptrealnodes or f.end in intersections:
                G.add_edge(f.start, f.end, requires = f.requires, weight = f.weight)
                yield Edge.seed(f.end, f.tip)
            else:
                yield f
    #print(G)
    #for t in nx.get_edge_attributes(G, 'requires').items(): print(t)
    #for t in nx.get_edge_attributes(G, 'weight').items(): print(t)
    maxkeys = (1 << (len(G) - 1 - len(intersections))) - 1
    #print(maxkeys)
    H = nx.DiGraph()
    sinks = []
    @bfs(('@', 0), cullkey = lambda x: x)
    def proc2(n):
        c, keys = n
        for e in G.edges(c, True):
            if keys | e[2]['requires'] == keys:
                dest = e[1], keys | keymasks.get(e[1], 0)
                H.add_edge(n, dest, weight = e[2]['weight'])
                if dest[1] != maxkeys:
                    yield dest
                else:
                    sinks.append(dest)
    #print(H)
    #print(nx.get_edge_attributes(H, 'weight'))
    #print(sinks)
    print(min(nx.shortest_path_length(H, ('@', 0), sink, weight = 'weight') for sink in sinks))

def main():
    for block in inpath().read_text().split('\n\n'):
        _mainimpl(block)
