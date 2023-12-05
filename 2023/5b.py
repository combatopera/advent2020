from adventlib import inpath, readchunks
import re

number = re.compile('[0-9]+')

class Range:

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def moveto(self, mr):
        off = mr.y - mr.start
        self.stop += off
        self.start += off
        return self

    def __repr__(self):
        return f"[{self.start},{self.stop})"

class MapRange(Range):

    def __init__(self, y, x, l):
        super().__init__(x, x + l)
        self.y = y

class Map:

    def __init__(self, chunk):
        self.ranges = [MapRange(*map(int, number.findall(l))) for l in chunk[1:]]

    def xform(self, ranges):
        for mr in self.ranges:
            nextranges = []
            for r in ranges:
                if r.start >= mr.start and r.stop <= mr.stop:
                    yield Range(r.start, r.stop).moveto(mr)
                elif r.start < mr.start and r.stop > mr.stop:
                    yield Range(mr.start, mr.stop).moveto(mr)
                    nextranges.append(Range(r.start, mr.start))
                    nextranges.append(Range(mr.stop, r.stop))
                elif r.start < mr.stop and r.stop > mr.stop:
                    yield Range(r.start, mr.stop).moveto(mr)
                    nextranges.append(Range(mr.stop, r.stop))
                elif r.start < mr.start and r.stop > mr.start:
                    yield Range(mr.start, r.stop).moveto(mr)
                    nextranges.append(Range(r.start, mr.start))
                else:
                    nextranges.append(r)
            ranges = nextranges
        for r in ranges:
            yield r

def main():
    with inpath().open() as f:
        (seedline,), *mapchunks = readchunks(f)
    v = list(map(int, number.findall(seedline)))
    ranges = [Range(x, x + l) for x, l in zip(v[::2], v[1::2])]
    maps = [Map(chunk) for chunk in mapchunks]
    for m in maps:
        ranges = list(m.xform(ranges))
    print(min(r.start for r in ranges))
