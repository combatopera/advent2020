from adventlib import inpath, Vector
import re

kernel = [Vector([x, y]) for x in range(-1, 2) for y in range(-1, 2) if x or y]

def lines():
    with inpath().open() as f:
        for y, l in enumerate(l.rstrip() for l in f):
            yield y, l

def main():
    symbolhalo = set()
    for y, l in lines():
        for m in re.finditer('[^0-9.]', l):
            u = Vector([m.start(), y])
            for v in kernel:
                symbolhalo.add(u + v)
    def g():
        def check():
            for i in range(len(m.group())):
                if Vector([m.start() + i, y]) in symbolhalo:
                    return True
        for y, l in lines():
            for m in re.finditer('[0-9]+', l):
                if check():
                    yield int(m.group())
    print(sum(g()))
