from adventlib import inpath, Vector
import networkx as nx

moves = [(x, y) for r in [range(-1, 2)] for x in r for y in r if abs(x) ^ abs(y)]

class Edge:

    @classmethod
    def popone(cls, grid):
        p = next(p for p in grid if '.' != grid[p])
        c = grid.pop(p)
        return cls(c, c, 0, p)

    @classmethod
    def _of(cls, *args):
        return cls(*args)

    def __init__(self, start, end, weight, tip):
        self.start = start
        self.end = end
        self.weight = weight
        self.tip = tip

    def popsteps(self, grid):
        for m in moves:
            q = self.tip + m
            if q in grid:
                yield self._of(self.start, grid.pop(q), self.weight + 1, q)

def main():
    for block in inpath().read_text().split('\n\n'):
        G = nx.Graph()
        grid = {}
        for y, line in enumerate(block.splitlines()):
            for x, c in enumerate(line):
                if '#' != c:
                    grid[Vector([x, y])] = c
        edges = [Edge.popone(grid)]
        while edges:
            nextedges = []
            for e in edges:
                for f in e.popsteps(grid):
                    if '.' != f.end:
                        G.add_edge(f.start, f.end, weight = f.weight)
                        nextedges.append(Edge(f.end, f.end, 0, f.tip))
                    else:
                        nextedges.append(f)
            edges = nextedges
        print(G)
