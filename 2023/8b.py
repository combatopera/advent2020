from adventlib import inpath, readchunks
from functools import reduce
from numpy import lcm
import operator, re

caps = re.compile('[0-9A-Z]{3}')

def main():
    with inpath().open() as f:
        (top,), rest = readchunks(f)
    chart = {k: dict(L = l, R = r) for line in rest for k, l, r in [caps.findall(line)]}
    def g():
        for key in chart:
            if key[-1] != 'A':
                continue
            steps = 0
            while key[-1] != 'Z':
                for c in top:
                    key = chart[key][c]
                steps += len(top)
            yield steps
    print(lcm.reduce(list(g())))
