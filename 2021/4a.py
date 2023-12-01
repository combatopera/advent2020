from adventlib import readchunks
from adventlib import inpath

emptyset = set()

class Board:

    def __init__(self, lines):
        rows = [[int(n) for n in l.split()] for l in lines]
        self.rows = [set(r) for r in rows]
        self.cols = [set(c) for c in zip(*rows)]

    def fire(self, n):
        for r in self.rows:
            r.discard(n)
        for c in self.cols:
            c.discard(n)
        return emptyset in self.rows or emptyset in self.cols

    def unmarked(self):
        for r in self.rows:
            yield from r

def main():
    with inpath().open() as f:
        i = readchunks(f)
        numbers, = ([int(n) for n in l.split(',')] for l in next(i))
        boards = [Board(lines) for lines in i]
    for n in numbers:
        for b in boards:
            if b.fire(n):
                print(sum(b.unmarked()) * n)
                return
