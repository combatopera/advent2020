from adventlib import intcos, intsin, Vector
from adventlib import inpath

class Grid(dict):

    kernel = [Vector([intcos(k), intsin(k)]) for k in range(4)]

    def _islow(self, k):
        for d in self.kernel:
            n = self.get(k + d)
            if n is not None and n <= self[k]:
                return
        return True

    def lowpoints(self):
        for k, n in self.items():
            if self._islow(k):
                yield n

def main():
    grid = Grid()
    for y, line in enumerate(inpath().read_text().splitlines()):
        for x, c in enumerate(line):
            grid[Vector([x, y])] = int(c)
    print(sum(1 + n for n in grid.lowpoints()))
