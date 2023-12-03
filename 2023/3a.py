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
        for y, l in lines():
            for m in re.finditer('[0-9]+', l):
                text = m.group()
                if any(Vector([m.start() + i, y]) in symbolhalo for i in range(len(text))):
                    yield int(text)
    print(sum(g()))
