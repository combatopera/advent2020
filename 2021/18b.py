#!/usr/bin/env python3

from collections import namedtuple
from pathlib import Path

class Null:

    def add(self, n):
        return n

class Address(namedtuple('BaseAddress', 'number index')): pass

class Number(list):

    class Int(int):

        def explode(self, *context):
            pass

        def addimpl(self, address, n, target):
            address.number[address.index] = type(self)(self + n)

        def split(self, address):
            if self >= 10:
                address.number[address.index] = Number([type(self)(self // 2), type(self)((self + 1) // 2)])
                return True

        def magnitude(self):
            return self

    zero = Int(0)

    @classmethod
    def xform(cls, obj):
        try:
            return cls(map(cls.xform, obj))
        except TypeError:
            return cls.Int(obj)

    def add(self, n):
        n = type(self)([self, n])
        while True:
            if not (n.explode() or n.split(None)):
                return n

    def explode(self, *context):
        if 4 != len(context):
            return any(n.explode(Address(self, i), *context) for i, n in enumerate(self))
        for index, n in enumerate(self):
            for address in context:
                if address.index == 1 - index:
                    address.number[index].addimpl(Address(address.number, index), n, 1 - index)
                    break
        context[0].number[context[0].index] = self.zero
        return True

    def addimpl(self, address, n, target):
        self[target].addimpl(Address(self, target), n, target)

    def split(self, address):
        return any(n.split(Address(self, i)) for i, n in enumerate(self))

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
