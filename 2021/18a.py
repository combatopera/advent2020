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
        fixme

    def magnitude(self):
        fixme

def main():
    n = Null()
    with Path('input', '18').open() as f:
        for line in f:
            n = n.add(Number.xform(eval(line)))
    print(n.magnitude())

if '__main__' == __name__:
    main()
