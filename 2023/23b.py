from adventlib import inpath, Vector

dirs = (1, 0), (0, 1), (-1, 0), (0, -1)

class Maze:

    def __init__(self, lines):
        self.ground = set()
        for y, l in enumerate(lines):
            for x, c in enumerate(l):
                if '#' != c:
                    self.ground.add((x, y))
        self.target = x - 1, y

    def walk(self, path, p):
        while True:
            if p == self.target:
                yield len(path) # Counting start instead of target.
                break
            path.add(p)
            next = []
            for d in dirs:
                q = p + d
                if q not in path and q in self.ground:
                    next.append(q)
            if 1 != len(next):
                for q in next:
                    yield from self.walk(path.copy(), q)
                break
            p, = next

def main():
    print(max(Maze(inpath().read_text().splitlines()).walk(set(), Vector([1, 0]))))
