from adventlib import inpath, Vector

gradients = {'>': [(1, 0)], 'v': [(0, 1)], '<': [(-1, 0)], '^': [(0, -1)]}
gradients['.'] = sum(gradients.values(), [])

class Maze:

    def __init__(self, lines):
        self.ground = {}
        for y, l in enumerate(lines):
            for x, c in enumerate(l):
                if '#' != c:
                    self.ground[x, y] = c
        self.target = x - 1, y

    def walk(self, path, p):
        while True:
            path[p] = len(path)
            next = []
            for d in gradients[self.ground[p]]:
                q = p + d
                if q not in path and q in self.ground:
                    next.append(q)
            if not next:
                yield path
                break
            if len(next) > 1:
                for q in next:
                    yield from self.walk(path.copy(), q)
                break
            p, = next

def main():
    m = Maze(inpath().read_text().splitlines())
    def g():
        for path in m.walk({}, Vector([1, 0])):
            n = path.get(m.target)
            if n is not None:
                yield n
    print(max(g()))
