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

    def walk(self, ground, path, p):
        while True:
            if p == self.target:
                yield len(path) # Counting start instead of target.
                break
            path.add(p)
            next = []
            for d in dirs:
                q = p + d
                if q not in path and q in ground:
                    next.append(q)
            if 1 != len(next):
                for q in next:
                    for n in self.walk(ground - path, set(), q):
                        yield len(path) + n
                break
            p, = next

def main():
    m = Maze(inpath().read_text().splitlines())
    print(max(m.walk(m.ground, set(), Vector([1, 0]))))
