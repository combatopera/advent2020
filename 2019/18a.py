from adventlib import inpath, Vector
from collections import namedtuple
from itertools import chain
from string import ascii_lowercase, ascii_uppercase
import networkx as nx

class Move:

    def __init__(self, off, weight = 1):
        self.off = off
        self.weight = weight

moves = list(map(Move, [(1, 0), (0, 1), (-1, 0), (0, -1)]))
middle = Vector([40, 40])
circle = {middle + (x, y) for x in range(-1, 2) for y in range(-1, 2) if x or y}
teleports = {
    middle: [Move(off, 3) for off in [(-1, -2), (1, -2), (-1, 2), (1, 2)]],
    middle + (-1, -2): [Move((1, -2), 4), Move((-1, 2), 4), Move((1, 2), 6)],
    middle + (1, -2): [Move((-1, -2), 4), Move((1, 2), 4), Move((-1, 2), 6)],
    middle + (-1, 2): [Move((-1, -2), 4), Move((1, 2), 4), Move((1, -2), 6)],
    middle + (1, 2): [Move((1, -2), 4), Move((-1, 2), 4), Move((-1, -2), 6)],
}

class Path:

    def __init__(self, history, tip, weight):
        self.lava = {*history, tip}
        self.tip = tip
        self.weight = weight

    def explore(self, grid):
        for m in chain(moves, teleports.get(self.tip, ())):
            q = self.tip + m.off
            if q not in circle and q not in self.lava and grid.chars[q] != '#':
                yield Path(self.lava, q, self.weight + m.weight)

class Node(namedtuple('BaseNode', 'c keys')):

    def edges(self, grid):
        doors = grid.alldoors - {c.upper() for c in self.keys}
        paths = [Path(set(), grid.points[self.c], 0)]
        while paths:
            nextpaths = []
            for path in paths:
                for q in path.explore(grid):
                    c = grid.chars[q.tip]
                    if c in doors:
                        pass
                    elif c in grid.allkeys:
                        yield self, self._make([c, frozenset(chain(self.keys, [c]))]), q.weight
                    else:
                        nextpaths.append(q)
            paths = nextpaths

    def __str__(self):
        return f"{self.c}({''.join(sorted(self.keys))})"

class Grid:

    source = Node('@', frozenset())

    def __init__(self, lines):
        self.chars = {}
        self.points = {}
        ofinterest = set(chain(ascii_lowercase, ['@']))
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                self.chars[x, y] = c
                if c in ofinterest:
                    self.points[c] = Vector([x, y])
        self.allkeys = self.points.keys() - {'@'}
        self.alldoors = set(c for s in [set(ascii_uppercase)] for c in self.chars.values() if c in s)

    def graph(self):
        G = nx.DiGraph()
        nodes = [self.source]
        explored = set()
        sinks = []
        while nodes:
            nextnodes = []
            for node in nodes:
                if node not in explored:
                    explored.add(node)
                    if node.keys == self.allkeys:
                        sinks.append(node)
                    else:
                        for source, target, weight in node.edges(self):
                            print(source, target, weight)
                            G.add_edge(source, target, weight = weight)
                            nextnodes.append(target)
            nodes = nextnodes
        return G, sinks

def _minpathlen(G, source, target):
    return nx.shortest_path_length(G, source, target, weight = 'weight')

def main():
    for block in inpath().read_text().split('\n\n'):
        grid = Grid(block.splitlines())
        G, sinks = grid.graph()
        print(min(_minpathlen(G, grid.source, target) for target in sinks))
