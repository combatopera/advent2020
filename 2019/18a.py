from adventlib import inpath, Vector
from diapyr.util import innerclass
from string import ascii_lowercase, ascii_uppercase
import networkx as nx

moves = (1, 0), (0, 1), (-1, 0), (0, -1)

class Grid:

    @innerclass
    class Node:

        @classmethod
        def _of(cls, *args):
            return cls(*args)

        def __init__(self, p, keys):
            self.p = p
            self.keys = keys

        def links(self):
            augdoors = self.alldoors - {c.upper() for c in self.keys} | {'#'}
            firsts = [q for m in moves for q in [self.p + m] if self.d[q] not in augdoors]
            for p in firsts:
                lava = {self.p, p}
                while True:
                    nexts = [q for m in moves for q in [p + m] if q not in lava and self.d[q] not in augdoors]
                    if not nexts:
                        break
                    p, = nexts
                    lava.add(p)
                    c = self.d[p]
                    if c in self.allkeys:
                        yield len(lava) - 1, self._of(p, self.keys | {c})
                        break

        def __str__(self):
            return f"{self.d[self.p]}({''.join(sorted(self.keys))})"

    def __init__(self):
        self.d = {}
        for y, line in enumerate(inpath().read_text().splitlines()):
            for x, c in enumerate(line):
                self.d[x, y] = c
        self.alldoors = set(c for s in [set(ascii_uppercase)] for c in self.d.values() if c in s)
        self.allkeys = set(c for s in [set(ascii_lowercase)] for c in self.d.values() if c in s)

    def nodes(self):
        ofinterest = self.allkeys | {'@'}
        for (x, y), c in self.d.items():
            if c in ofinterest:
                yield self.Node(Vector((x, y)), self.allkeys & {c})

def main():
    G = nx.Graph()
    grid = Grid()
    nodes = list(grid.nodes())
    seen = set()
    while nodes:
        nextnodes = []
        for node in nodes:
            if str(node) not in seen and node.keys != grid.allkeys:
                seen.add(str(node))
                for weight, link in node.links():
                    G.add_edge(str(node), str(link), weight = weight)
                    nextnodes.append(link)
        nodes = nextnodes
    for target in G.nodes:
        if target.endswith(f"({''.join(sorted(grid.allkeys))})"):
            print(target, nx.shortest_path_length(G, '@()', target, weight = 'weight'))
