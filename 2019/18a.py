from adventlib import inpath, Vector
from collections import namedtuple
from itertools import chain
from string import ascii_lowercase, ascii_uppercase
import networkx as nx

moves = (1, 0), (0, 1), (-1, 0), (0, -1)

class Node(namedtuple('BaseNode', 'c keys')):

    def links(self, grid):
        self_p = grid.points[self.c]
        walls = grid.alldoors - {c.upper() for c in self.keys} | {'#'}
        firsts = [q for m in moves for q in [self_p + m] if grid.chars[q] not in walls]
        for p in firsts:
            lava = {self_p, p}
            while True:
                nexts = [q for m in moves for q in [p + m] if q not in lava and grid.chars[q] not in walls]
                if not nexts:
                    break
                p, = nexts
                lava.add(p)
                c = grid.chars[p]
                if c in grid.allkeys:
                    yield len(lava) - 1, self._make([c, frozenset(chain(self.keys, [c]))])
                    break

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
                        G.add_edge(node, link, weight = weight)
                        nextnodes.append(link)
            nodes = nextnodes
        return G

def main():
    grid = Grid(inpath().read_text().splitlines())
    G = grid.graph()
    print(min(nx.shortest_path_length(G, grid.source, target, weight = 'weight') for target in G.nodes if target.keys == grid.allkeys))
