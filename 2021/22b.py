from adventlib import inpath
import re

class Box:

    def __init__(self, x1, x2, y1, y2, z1, z2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2

    def valid(self):
        return self.x1 < self.x2 and self.y1 < self.y2 and self.z1 < self.z2

    def sub(self, that):
        if self.x1 < that.x2 and that.x1 < self.x2 and self.y1 < that.y2 and that.y1 < self.y2 and self.z1 < that.z2 and that.z1 < self.z2:
            def g():
                yield self.x1, self.x2, self.y1, self.y2, self.z1, that.z1
                yield self.x1, self.x2, self.y1, self.y2, that.z2, self.z2
                z = max(self.z1, that.z1), min(self.z2, that.z2)
                yield [self.x1, that.x1, self.y1, self.y2, *z]
                yield [that.x2, self.x2, self.y1, self.y2, *z]
                x = max(self.x1, that.x1), min(self.x2, that.x2)
                yield [*x, self.y1, that.y1, *z]
                yield [*x, that.y2, self.y2, *z]
            for v in g():
                b = type(self)(*v)
                if b.valid():
                    yield b
        else:
            yield self

    def volume(self):
        return (self.x2 - self.x1) * (self.y2 - self.y1) * (self.z2 - self.z1)

class Reactor:

    def __init__(self):
        self.boxes = []

    def apply(self, ison, box):
        boxes = []
        for b in self.boxes:
            boxes.extend(b.sub(box))
        if ison:
            boxes.append(box)
        self.boxes[:] = boxes

def main():
    r = Reactor()
    with inpath().open() as f:
        for i, l in enumerate(f):
            command, l = l.split()
            v = list(map(int, re.findall('-?[0-9]+', l)))
            r.apply('on' == command, Box(v[0], v[1]+1, v[2], v[3]+1, v[4], v[5]+1))
    print(sum(b.volume() for b in r.boxes))
