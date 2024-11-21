from adventlib import inpath, Vector

moves = (1, 0), (0, 1), (-1, 0), (0, -1)

class Node:

    @classmethod
    def _of(cls, *args):
        return cls(*args)

    def __init__(self, edge, p):
        print(edge, p)
        self.children = []
        self.edge = edge
        self.p = p

    def explore(self, grid, lava):
        lava.add(self.p)
        for p in (q for m in moves for q in [self.p + m] if q in grid and q not in lava):
            path = []
            while True:
                if '.' != grid[p]:
                    self.children.append(self._of(len(path), p))
                    break
                v = [q for m in moves for q in [p + m] if q in grid and q not in lava and q not in path]
                if not v:
                    path.append(p)
                    break
                if len(v) > 1:
                    self.children.append(self._of(len(path), p))
                    break
                path.append(p)
                p = v[0]
            lava.update(path)
        for child in self.children:
            child.explore(grid, lava)

def main():
    grid = {}
    for y, line in enumerate(inpath().read_text().splitlines()):
        for x, c in enumerate(line):
            if '#' != c:
                grid[x, y] = c
                if '@' == c:
                    you = Vector([x, y])
    tree = Node(None, you)
    tree.explore(grid, set())
