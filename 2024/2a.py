from adventlib import inpath
from itertools import islice

def main():
    def safe():
        for l in inpath().read_text().splitlines():
            v = list(map(int, l.split()))
            diffs = {x - y for x, y in zip(v, islice(v, 1, None))}
            if diffs <= {1, 2, 3} or diffs <= {-1, -2, -3}:
                yield
    print(sum(1 for _ in safe()))
