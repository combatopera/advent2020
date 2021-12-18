#!/usr/bin/env python3

from collections import namedtuple
from pathlib import Path

class Address(namedtuple('BaseAddress', 'number index')):

    def mirror(self):
        return type(self)(self.number, 1 - self.index)

    def replace(self, n):
        self.number[self.index] = n

def _invoker(name):
    return lambda self, *args: getattr(self.number[self.index], name)(self, *args)

for name in 'explode', 'addimpl', 'split':
    setattr(Address, name, _invoker(name))

class Int(int):

    def clone(self):
        return self

    def explode(self, *context):
        pass

    def addimpl(self, address, index, n):
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

    def _addresses(self):
        for i in range(len(self)):
            yield Address(self, i)

    def clone(self):
        return type(self)(n.clone() for n in self)

    def add(self, that):
        res = type(self)(n.clone() for n in [self, that])
        while res.explode() or res.split(None):
            pass
        return res

    def explode(self, *context):
        if 4 != len(context):
            return any(a.explode(*context) for a in self._addresses())
        for index, n in enumerate(self):
            for address in context:
                if address.index == 1 - index:
                    address.mirror().addimpl(1 - index, n)
                    break
        context[0].replace(zero)
        return True

    def addimpl(self, address, index, n):
        Address(self, index).addimpl(index, n)

    def split(self, address):
        return any(a.split() for a in self._addresses())

    def magnitude(self):
        return sum(k * n.magnitude() for k, n in zip([3, 2], self))

def main():
    numbers = [Number.xform(eval(l)) for l in Path('input', '18').read_text().splitlines()]
    print(max(m.add(n).magnitude() for m in numbers for n in numbers if m is not n))

if '__main__' == __name__:
    main()
