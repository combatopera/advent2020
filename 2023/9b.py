from adventlib import inpath, differentiate
from functools import reduce
import re

def extrapolate(v):
    derivatives = [v]
    while any(derivatives[-1]):
        derivatives.append(differentiate(derivatives[-1]))
    return reduce(lambda first, d: d[0] - first, reversed(derivatives), 0)

def main():
    def g():
        with inpath().open() as f:
            for l in f:
                yield extrapolate(list(map(int, re.findall('[0-9-]+', l))))
    print(sum(g()))
