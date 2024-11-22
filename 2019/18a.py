from adventlib import inpath, Vector
from collections import namedtuple
from diapyr.util import innerclass
from itertools import chain
from string import ascii_lowercase, ascii_uppercase
import networkx as nx

moves = (1, 0), (0, 1), (-1, 0), (0, -1)

class Node(namedtuple('BaseNode', 'c keys')):

    def links(self, grid):
        self_p = grid.lookup[self.c]
        augdoors = grid.alldoors - {c.upper() for c in self.keys} | {'#'}
        firsts = [q for m in moves for q in [self_p + m] if grid.d[q] not in augdoors]
        for p in firsts:
            lava = {self_p, p}
            while True:
                nexts = [q for m in moves for q in [p + m] if q not in lava and grid.d[q] not in augdoors]
                if not nexts:
                    break
                p, = nexts
                lava.add(p)
                c = grid.d[p]
                if c in grid.allkeys:
                    yield len(lava) - 1, self._make([c, frozenset(chain(self.keys, [c]))])
                    break

class Grid:

    def __init__(self):
        self.d = {}
        self.lookup = {}
        for y, line in enumerate(inpath().read_text().splitlines()):
            for x, c in enumerate(line):
                self.d[x, y] = c
                if '@' == c or c in ascii_lowercase:
                    self.lookup[c] = Vector([x, y])
        self.alldoors = set(c for s in [set(ascii_uppercase)] for c in self.d.values() if c in s)
        self.allkeys = set(c for s in [set(ascii_lowercase)] for c in self.d.values() if c in s)

    def graph(self):
        G = nx.Graph()
        nodes = [Node(c, frozenset(self.allkeys & {c})) for chars in [self.allkeys | {'@'}] for (x, y), c in self.d.items() if c in chars]
        seen = set()
        while nodes:
            nextnodes = []
            for node in nodes:
                if node not in seen and node.keys != self.allkeys:
                    seen.add(node)
                    for weight, link in node.links(self):
                        G.add_edge(node, link, weight = weight)
                        nextnodes.append(link)
            nodes = nextnodes
        return G

def main():
    grid = Grid()
    G = grid.graph()
    source = Node('@', frozenset())
    for target in G.nodes:
        if target.keys == grid.allkeys:
            print(target, nx.shortest_path_length(G, source, target, weight = 'weight'))
