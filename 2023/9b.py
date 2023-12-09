from adventlib import inpath, differentiate
import re

def extrapolate(v):
    derivatives = [v]
    while any(derivatives[-1]):
        derivatives.append(differentiate(derivatives[-1]))
    first = 0
    for d in reversed(derivatives):
        first = d[0] - first
    return first

def main():
    def g():
        with inpath().open() as f:
            for l in f:
                yield extrapolate(list(map(int, re.findall('[0-9-]+', l))))
    print(sum(g()))
