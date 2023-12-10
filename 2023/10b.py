from adventlib import inpath, Vector

shapes = {k: set(map(Vector, v)) for k, v in {
    '|': [(0, -1), (0, 1)],
    '-': [(-1, 0), (1, 0)],
    'L': [(0, -1), (1, 0)],
    'J': [(0, -1), (-1, 0)],
    '7': [(0, 1), (-1, 0)],
    'F': [(0, 1), (1, 0)],
}.items()}
barriers = {c for c, shape in shapes.items() if (0, -1) in shape}

class Grid:

    def __init__(self, lines):
        self.reference = {}
        self.tiletofriends = {}
        for y, l in enumerate(lines):
            for x, c in enumerate(l):
                t = Vector([x, y])
                self.reference[t] = c
                shape = shapes.get(c)
                if shape is not None:
                    self.tiletofriends[t] = [t + d for d in shape]
                elif 'S' == c:
                    self.start = t
        self.w = x + 1
        self.h = y + 1
        self.tiletofriends[self.start] = [t for t, friends in self.tiletofriends.items() if self.start in friends]
        startshape = {t - self.start for t in self.tiletofriends[self.start]}
        self.reference[self.start], = (c for c, shape in shapes.items() if shape == startshape)
        self.loop = set(self._getloop())

    def _anynext(self, exclude, t):
        for u in self.tiletofriends[t]:
            if exclude != u:
                return u

    def _getloop(self):
        prev, t = None, self.start
        while True:
            yield t
            prev, t = t, self._anynext(prev, t)
            if self.start == t:
                break

    def inside(self):
        inside = set()
        for y in range(self.h):
            for x in range(1, self.w):
                left = x - 1, y
                leftisin = left in inside
                between = self.reference[left] if left in self.loop else '.'
                if leftisin ^ (between in barriers):
                    inside.add((x, y))
        return inside - self.loop

def main():
    print(len(Grid(inpath().read_text().splitlines()).inside()))
