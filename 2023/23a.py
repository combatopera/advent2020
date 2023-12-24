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
            if p == self.target:
                yield len(path) # Counting start instead of target.
                break
            path.add(p)
            next = []
            for d in gradients[self.ground[p]]:
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
