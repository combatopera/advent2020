from adventlib import inpath, readchunks
import re

number = re.compile('[0-9]+')

class Range:

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

class MapRange(Range):

    def __init__(self, y, x, l):
        super().__init__(x, x + l)
        self.off = y - x

    def _shift(self, start, stop):
        return Range(self.off + start, self.off + stop)

    def xform(self, unxformed, r):
        if r.start >= self.start and r.stop <= self.stop:
            yield self._shift(r.start, r.stop)
        elif r.start < self.start and r.stop > self.stop:
            yield self._shift(self.start, self.stop)
            unxformed.append(Range(r.start, self.start))
            unxformed.append(Range(self.stop, r.stop))
        elif r.start < self.stop and r.stop > self.stop:
            yield self._shift(r.start, self.stop)
            unxformed.append(Range(self.stop, r.stop))
        elif r.start < self.start and r.stop > self.start:
            yield self._shift(self.start, r.stop)
            unxformed.append(Range(r.start, self.start))
        else:
            unxformed.append(r)

class Map:

    def __init__(self, chunk):
        self.ranges = [MapRange(*map(int, number.findall(l))) for l in chunk[1:]]

    def xform(self, unxformed):
        for mr in self.ranges:
            ranges, unxformed = unxformed, []
            for r in ranges:
                yield from mr.xform(unxformed, r)
        for r in unxformed:
            yield r

def main():
    with inpath().open() as f:
        (seedline,), *mapchunks = readchunks(f)
    v = list(map(int, number.findall(seedline)))
    ranges = [Range(x, x + l) for x, l in zip(v[::2], v[1::2])]
    for chunk in mapchunks:
        ranges = list(Map(chunk).xform(ranges))
    print(min(r.start for r in ranges))
