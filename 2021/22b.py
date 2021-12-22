#!/usr/bin/env python3

from pathlib import Path
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
            w1 = type(self)(self.x1, self.x2, self.y1, self.y2, self.z1, that.z1)
            w2 = type(self)(self.x1, self.x2, self.y1, self.y2, that.z2, self.z2)
            u1 = type(self)(self.x1, that.x1, self.y1, self.y2, max(self.z1, that.z1), min(self.z2, that.z2))
            u2 = type(self)(that.x2, self.x2, self.y1, self.y2, max(self.z1, that.z1), min(self.z2, that.z2))
            v1 = type(self)(max(self.x1, that.x1), min(self.x2, that.x2), self.y1, that.y1, max(self.z1, that.z1), min(self.z2, that.z2))
            v2 = type(self)(max(self.x1, that.x1), min(self.x2, that.x2), that.y2, self.y2, max(self.z1, that.z1), min(self.z2, that.z2))
            for b in w1, w2, u1, u2, v1, v2:
                if b.valid():
                    yield b
        else:
            yield self

    def volume(self):
        return (self.x2 - self.x1) * (self.y2 - self.y1) * (self.z2 - self.z1)

    def __str__(self):
        return ' '.join(map(str, [self.x1, self.x2-1, self.y1, self.y2-1, self.z1, self.z2-1]))

class Reactor:

    def __init__(self):
        self.boxes = []

    def apply(self, command, box):
        boxes = []
        for b in self.boxes:
            boxes.extend(b.sub(box))
        if 'on' == command:
            boxes.append(box)
        self.boxes[:] = boxes

def main():
    r = Reactor()
    with Path('input', '22').open() as f:
        for i, l in enumerate(f):
            command, l = l.split()
            v = list(map(int, re.findall('-?[0-9]+', l)))
            b = Box(v[0], v[1]+1, v[2], v[3]+1, v[4], v[5]+1)
            r.apply(command, b)
    print(sum(b.volume() for b in r.boxes))

if '__main__' == __name__:
    main()
