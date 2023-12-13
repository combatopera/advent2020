from adventlib import inpath, readchunks
from itertools import islice

class Pattern:

    @property
    def w(self):
        return len(self.cols)

    @property
    def h(self):
        return len(self.rows)

    def __init__(self, chunk):
        self.cols = list(zip(*chunk))
        self.rows = chunk

    def score(self):
        def g():
            for x in range(1, self.w):
                if all(self.cols[x - 1 - k] == self.cols[x + k] for k in range(min(x, self.w - x))):
                    yield x
            for y in range(1, self.h):
                if all(self.rows[y - 1 - k] == self.rows[y + k] for k in range(min(y, self.h - y))):
                    yield y * 100
        s, = g()
        return s

def main():
    def g():
        with inpath().open() as f:
            for chunk in readchunks(f):
                yield Pattern(chunk).score()
    print(sum(g()))
