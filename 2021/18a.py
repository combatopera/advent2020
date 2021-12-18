#!/usr/bin/env python3

from pathlib import Path

class Null:

    def add(self, n):
        return n

class Number(tuple):

    class Int(int):

        def magnitude(self):
            return self

    @classmethod
    def xform(cls, obj):
        try:
            return cls(map(cls.xform, obj))
        except TypeError:
            return cls.Int(obj)

    def add(self, n):
        n = type(self)([self, n])
        while True:
            m = n.ereduce()
            if m is not None:
                n = m
                continue
            m = n.sreduce()
            if m is not None:
                n = m
                continue
            return n

    def magnitude(self):
        return 3 * self[0].magnitude() + 2 * self[1].magnitude()

def main():
    n = Null()
    with Path('input', '18').open() as f:
        for line in f:
            n = n.add(Number.xform(eval(line)))
    print(n.magnitude())

if '__main__' == __name__:
    main()
