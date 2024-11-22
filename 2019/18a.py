from adventlib import inpath, Vector
from collections import namedtuple
from itertools import chain
from string import ascii_lowercase, ascii_uppercase
import networkx as nx

moves = (1, 0), (0, 1), (-1, 0), (0, -1)

class Path:

    def __init__(self, history, tip):
        self.lava = {*history, tip}
        self.tip = tip

    def weight(self):
        return len(self.lava) - 1

    def explore(self, grid):
        for m in moves:
            q = self.tip + m
            if q not in self.lava and grid.chars[q] != '#':
                yield Path(self.lava, q)

class Node(namedtuple('BaseNode', 'c keys')):

    def links(self, grid):
        doors = grid.alldoors - {c.upper() for c in self.keys}
        paths = [Path(set(), grid.points[self.c])]
        while paths:
            nextpaths = []
            for path in paths:
                for q in path.explore(grid):
                    c = grid.chars[q.tip]
                    if c in doors:
                        pass
                    elif c in grid.allkeys:
                        yield q.weight(), self._make([c, frozenset(chain(self.keys, [c]))])
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
        G = nx.Graph()
        nodes = [self.source, *(Node(c, frozenset([c])) for c in self.allkeys)]
        seen = set()
        while nodes:
            nextnodes = []
            for node in nodes:
                if node not in seen and node.keys != self.allkeys:
                    seen.add(node)
                    for weight, link in node.links(self):
                        #print(node, weight, link)
                        G.add_edge(node, link, weight = weight)
                        nextnodes.append(link)
            nodes = nextnodes
        return G

def main():
    for block in inpath().read_text().split('\n\n'):
        grid = Grid(block.splitlines())
        G = grid.graph()
        print(min(nx.shortest_path_length(G, grid.source, target, weight = 'weight') for target in G.nodes if target.keys == grid.allkeys))
