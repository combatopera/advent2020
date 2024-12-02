from adventlib import inpath
from itertools import islice

def main():
    def safe(l):
        def g():
            for i, x in enumerate(v):
                if i != remove:
                    yield x
        v = list(map(int, l.split()))
        for remove in range(-1, len(v)):
            diffs = {x - y for x, y in zip(g(), islice(g(), 1, None))}
            if diffs <= {1, 2, 3} or diffs <= {-1, -2, -3}:
                return True
    print(sum(1 for l in inpath().read_text().splitlines() if safe(l)))
