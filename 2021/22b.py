#!/usr/bin/env python3

from pathlib import Path
import re

class Command:

    def __init__(self, on, u, v):
        self.on = on
        self.u = u
        self.v = v

class Reactor:

    def __init__(self, xplanes, yplanes, zplanes):
        self.on = set()
        self.xplanes = {x: i for i, x in enumerate(sorted(xplanes))}
        self.yplanes = {x: i for i, x in enumerate(sorted(yplanes))}
        self.zplanes = {x: i for i, x in enumerate(sorted(zplanes))}

    def apply(self, command):
        x1 = self.xplanes[command.u[0]]
        x2 = self.xplanes[command.v[0]+1]
        y1 = self.yplanes[command.u[1]]
        y2 = self.yplanes[command.v[1]+1]
        z1 = self.zplanes[command.u[2]]
        z2 = self.zplanes[command.v[2]+1]
        for x in range(x1, x2):
            for y in range(y1, y2):
                for z in range(z1, z2):
                    (self.on.add if command.on else self.on.discard)((x, y, z))

def main():
    commands = []
    with Path('input', '22').open() as f:
        for l in f:
            command, l = l.split()
            v = list(map(int, re.findall('-?[0-9]+', l)))
            commands.append(Command('on' == command, v[::2], v[1::2]))
    xplanes = set()
    yplanes = set()
    zplanes = set()
    for c in commands:
        xplanes.add(c.u[0])
        xplanes.add(c.v[0]+1)
        yplanes.add(c.u[1])
        yplanes.add(c.v[1]+1)
        zplanes.add(c.u[2])
        zplanes.add(c.v[2]+1)
    r = Reactor(xplanes, yplanes, zplanes)
    for c in commands:
        print(c)
        r.apply(c)
        print(len(r.on))

if '__main__' == __name__:
    main()
