from adventlib import inpath, readchunks

class Paper(set):

    def fold(self, a, n):
        for v in list(self):
            if v[a] > n:
                self.remove(v)
                self.add(tuple(2 * n - x if a == i else x for i, x in enumerate(v)))

    def lines(self):
        w = max(v[0] for v in self) + 1
        for y in range(max(v[1] for v in self) + 1):
            yield ''.join('#' if (x, y) in self else '.' for x in range(w))

def main():
    with inpath().open() as f:
        dots, folds = readchunks(f)
    paper = Paper(tuple(map(int, d.split(','))) for d in dots)
    for fold in folds:
        axis, n = fold.split('=')
        paper.fold(0 if 'x' == axis[-1] else 1, int(n))
    for line in paper.lines():
        print(line)
