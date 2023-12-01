from collections import Counter
from adventlib import inpath

def main():
    sums = Counter()
    n = 0
    with inpath().open() as f:
        for line in f:
            for i, c in enumerate(line.rstrip()):
                sums[i] += ord(c)
            n += 1
    threshold = sum(ord(c) for c in '01') * n / 2
    g = sum((x > threshold) * (1 << (len(sums) - i - 1)) for i, x in sums.items())
    e = sum((x < threshold) * (1 << (len(sums) - i - 1)) for i, x in sums.items())
    print(g * e)
