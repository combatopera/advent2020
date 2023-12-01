from adventlib import inpath
import re

def _clamp(u, v, i):
    return range(max(-50, u[i]), min(50, v[i]) + 1)

class Reactor:

    def __init__(self):
        self.on = set()

    def do(self, command, minv, maxv):
        for x in _clamp(minv, maxv, 0):
            for y in _clamp(minv, maxv, 1):
                for z in _clamp(minv, maxv, 2):
                    (self.on.add if 'on' == command else self.on.discard)((x, y, z))

def main():
    r = Reactor()
    with inpath().open() as f:
        for l in f:
            command, l = l.split()
            v = list(map(int, re.findall('-?[0-9]+', l)))
            r.do(command, v[::2], v[1::2])
    print(len(r.on))
