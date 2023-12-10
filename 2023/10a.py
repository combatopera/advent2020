from adventlib import inpath

class Grid:

    def __init__(self, lines):
        self.tiletofriends = {}
        for y, l in enumerate(lines):
            for x, c in enumerate(l):
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
    n = Grid(inpath().read_text().splitlines()).looplen()
    assert 0 == n & 1
    print(n // 2)
