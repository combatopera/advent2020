from adventlib import inpath, Vector

shapes = {k: set(map(Vector, v)) for k, v in {
    '|': [(0, -1), (0, 1)],
    '-': [(-1, 0), (1, 0)],
    'L': [(0, -1), (1, 0)],
    'J': [(0, -1), (-1, 0)],
    '7': [(0, 1), (-1, 0)],
    'F': [(0, 1), (1, 0)],
}.items()}

class Grid:

    def __init__(self, lines):
        self.tiletofriends = {}
        for y, l in enumerate(lines):
            for x, c in enumerate(l):
                t = Vector([x, y])
                shape = shapes.get(c)
                if shape is not None:
                    self.tiletofriends[t] = [t + d for d in shape]
                elif 'S' == c:
                    self.start = t
        self.tiletofriends[self.start] = [t for t, friends in self.tiletofriends.items() if self.start in friends]

    def _anynext(self, exclude, t):
        for u in self.tiletofriends[t]:
            if exclude != u:
                return u

    def looplen(self):
        prev, t = None, self.start
        n = 0
        while True:
            prev, t = t, self._anynext(prev, t)
            n += 1
            if self.start == t:
                break
        return n

def main():
    n, r = divmod(Grid(inpath().read_text().splitlines()).looplen(), 2)
    assert not r
    print(n)
