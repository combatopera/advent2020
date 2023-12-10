from adventlib import inpath

class Grid:

    def __init__(self, lines):
        self.reference = {}
        self.tiletofriends = {}
        for y, l in enumerate(lines):
            for x, c in enumerate(l):
                self.reference[x, y] = c
                if '|' == c:
                    self.tiletofriends[x, y] = [(x, y - 1), (x, y + 1)]
                elif '-' == c:
                    self.tiletofriends[x, y] = [(x - 1, y), (x + 1, y)]
                elif 'L' == c:
                    self.tiletofriends[x, y] = [(x, y - 1), (x + 1, y)]
                elif 'J' == c:
                    self.tiletofriends[x, y] = [(x, y - 1), (x - 1, y)]
                elif '7' == c:
                    self.tiletofriends[x, y] = [(x, y + 1), (x - 1, y)]
                elif 'F' == c:
                    self.tiletofriends[x, y] = [(x, y + 1), (x + 1, y)]
                elif 'S' == c:
                    self.start = x, y
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
