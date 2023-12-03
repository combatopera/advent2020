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
            halo = set()
            for i in range(len(m.group())):
                u = Vector([m.start() + i, y])
                for v in kernel:
                    halo.add(u + v)
            value = int(m.group())
            for u in halo:
                numberhalo[u].append(value)
    def g():
        for y, l in lines():
            for m in re.finditer('[^0-9.]', l):
                values = numberhalo[Vector([m.start(), y])]
                if 2 == len(values):
                    yield reduce(operator.mul, values)
    print(sum(g()))
