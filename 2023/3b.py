from adventlib import inpath, Vector
from collections import defaultdict
from functools import reduce
import operator, re

kernel = [Vector([x, y]) for x in range(-1, 2) for y in range(-1, 2) if x or y]

def lines():
    with inpath().open() as f:
        for y, l in enumerate(l.rstrip() for l in f):
            yield y, l

def main():
    numberhalo = defaultdict(list)
    for y, l in lines():
        for m in re.finditer('[0-9]+', l):
            text = m.group()
            value = int(text)
            footprint = {Vector([m.start() + i, y]) for i in range(len(text))}
            for w in {u + v for u in footprint for v in kernel}:
                if w not in footprint:
                    numberhalo[w].append(value)
    def g():
        for y, l in lines():
            for m in re.finditer('[^0-9.]', l):
                values = numberhalo[Vector([m.start(), y])]
                if 2 == len(values):
                    yield reduce(operator.mul, values)
    print(sum(g()))
