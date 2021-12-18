#!/usr/bin/env python3

from collections import namedtuple
from pathlib import Path

class Address(namedtuple('BaseAddress', 'number index')):

    def replace(self, n):
        self.number[self.index] = n

    def __getattr__(self, name):
        return lambda *args: getattr(self.number[self.index], name)(self, *args)

class Int(int):

    def clone(self):
        return self

    def explode(self, *context):
        pass

    def addimpl(self, address, n, target):
        address.replace(type(self)(self + n))

    def split(self, address):
        if self >= 10:
            address.replace(Number([type(self)(self // 2), type(self)((self + 1) // 2)]))
            return True

    def magnitude(self):
        return self

zero = Int(0)

class Number(list):

    @classmethod
    def xform(cls, obj):
        try:
            return cls(map(cls.xform, obj))
        except TypeError:
            return Int(obj)

    def clone(self):
        return type(self)(n.clone() for n in self)

    def add(self, that):
        res = type(self)(n.clone() for n in [self, that])
        while res.explode() or res.split(None):
            pass
        return res

    def explode(self, *context):
        if 4 != len(context):
            return any(Address(self, i).explode(*context) for i, _ in enumerate(self))
        for index, n in enumerate(self):
            for address in context:
                if address.index == 1 - index:
                    address.number[index].addimpl(Address(address.number, index), n, 1 - index)
                    break
        context[0].replace(zero)
        return True

    def addimpl(self, address, n, target):
        self[target].addimpl(Address(self, target), n, target)

    def split(self, address):
        return any(n.split(Address(self, i)) for i, n in enumerate(self))

    def magnitude(self):
        return sum(k * n.magnitude() for k, n in zip([3, 2], self))

class Null:

    def add(self, n):
        return n

def main():
    n = Null()
    with Path('input', '18').open() as f:
        for line in f:
            n = n.add(Number.xform(eval(line)))
    print(n.magnitude())

if '__main__' == __name__:
    main()
