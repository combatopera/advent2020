from adventlib import inpath, readchunks
import re

number = re.compile('[0-9]+')

class Map:

    class Range:

        def __init__(self, y, x, l):
            self.r = range(x, x + l)
            self.y = y

        def xform(self, x):
            if x in self.r:
                return x - self.r.start + self.y

    def __init__(self, chunk):
        self.ranges = [self.Range(*map(int, number.findall(l))) for l in chunk[1:]]

    def xform(self, x):
        for r in self.ranges:
            y = r.xform(x)
            if y is not None:
                return y
        return x

def main():
    def locations():
        for n in map(int, number.findall(seedline)):
            for m in maps:
                n = m.xform(n)
            yield n
    with inpath().open() as f:
        (seedline,), *mapchunks = readchunks(f)
    maps = [Map(chunk) for chunk in mapchunks]
    print(min(locations()))
