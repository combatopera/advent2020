from adventlib import inpath, Vector
from itertools import islice
import networkx as nx

dirs = [1, 0], [0, 1], [-1, 0], [0, -1]

class Maze:

    source = Vector([1, 0])

    def __init__(self, lines):
        self.ground = set()
        for y, l in enumerate(lines):
            for x, c in enumerate(l):
                if '#' != c:
                    self.ground.add((x, y))
        self.target = x - 1, y

    def graph(self):
        G = nx.Graph()
        lava = {self.source}
        nodes = [self.source]
        while nodes:
            node = nodes.pop(0)
            for d in dirs:
                p = node + d
                if p in self.ground and p not in lava:
                    break
            else:
                continue
            worm = {node, p}
            while True:
                v = [q for d in dirs for q in [p + d] if q in self.ground and q not in worm]
                if not v:
                    break
                if len(v) > 1:
                    lava.add(p)
                    for q in v:
                        if q not in lava:
                            nodes.append(p)
                    break
                p, = v
                worm.add(p)
            worm.remove(node)
            worm.remove(p)
            G.add_edge(node, p, weight = len(worm))
            lava.update(worm)
        return G

def main():
    m = Maze(inpath().read_text().splitlines())
    G = m.graph()
    weights = nx.get_edge_attributes(G, 'weight')
    for e, w in list(weights.items()):
        weights[e[1], e[0]] = w
    def lengths():
        for path in nx.all_simple_paths(G, m.source, m.target):
            yield sum(weights[e] + 1 for e in zip(path, islice(path, 1, None)))
    print(max(lengths()))
