from adventlib import inpath, Vector

shapes = {k: list(map(Vector, v)) for k, v in {
    '|': [(0, -1), (0, 1)],
    '-': [(-1, 0), (1, 0)],
    'L': [(0, -1), (1, 0)],
    'J': [(0, -1), (-1, 0)],
    '7': [(0, 1), (-1, 0)],
    'F': [(0, 1), (1, 0)],
}.items()}

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
        self.loop = set(self._getloop())

    def _anynext(self, exclude, t):
        for u in self.tiletofriends[t]:
            if exclude != u:
                return u

    def _getloop(self):
        t, u = None, self.start
        while True:
            yield u
            t, u = u, self._anynext(t, u)
            if self.start == u:
                break

    def inside(self):
        inside = set()
        for y in range(self.h):
            for x in range(1, self.w):
                left = x - 1, y
                leftisin = left in inside
                between = self.reference[left] if left in self.loop else '.'
                if between in '-7F.':
                    thisisin = leftisin
                elif between in '|LJ':
                    thisisin = not leftisin
                elif 'S' == between:
                    up = x, y - 1
                    upisin = up in inside
                    between = self.reference[up] if up in self.loop else '.'
                    if between in '|LF.':
                        thisisin = upisin
                    elif between in '-J7':
                        thisisin = not upisin
                    else:
                        raise Exception
                if thisisin:
                    inside.add((x, y))
        return inside - self.loop

def main():
    print(len(Grid(inpath().read_text().splitlines()).inside()))
