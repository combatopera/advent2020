#!/usr/bin/env python3

from adventlib import readchunks
from pathlib import Path

class Paper(set):

    def fold(self, a, n):
        for v in list(self):
            if v[a] > n:
                self.remove(v)
                self.add(tuple(2 * n - x if a == i else x for i, x in enumerate(v)))

def main():
    with Path('input', '13').open() as f:
        dots, folds = readchunks(f)
    paper = Paper({tuple(map(int, d.split(','))) for d in dots})
    for fold in folds[:1]:
        axis, n = fold.split('=')
        paper.fold(0 if 'x' == axis[-1] else 1, int(n))
    print(len(paper))

if '__main__' == __name__:
    main()
