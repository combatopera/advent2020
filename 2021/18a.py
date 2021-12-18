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

        def add(self, address, n):
            address.number[address.index] = type(self)(self + n)

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
            if not (n.explode() or n.sreduce()):
                return n

    def explode(self, *context):
        if 4 != len(context):
            return any(n.explode(Address(self, i), *context) for i, n in enumerate(self))
        for index, n in enumerate(self):
            for address in context:
                if address.index == 1 - index:

                    print(address.number[index], '.add', Address(address.number, index), n)

                    address.number[index].add(Address(address.number, index), n)
                    break



        context[0].number[context[0].index] = self.zero
        return True

    def add(self, address, n):
        self[1 - address.index].add(Address(self, 1 - address.index), n)

    def magnitude(self):
        return 3 * self[0].magnitude() + 2 * self[1].magnitude()

def main():
    for n in '[[[[[9,8],1],2],3],4]','[7,[6,[5,[4,[3,2]]]]]','[[6,[5,[4,[3,2]]]],1]','[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]','[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]':
        n=Number.xform(eval(n))
        print(n)
        n.explode()
        print(n)
        print()
    dthdfgd

    n = Null()
    with Path('input', '18').open() as f:
        for line in f:
            n = n.add(Number.xform(eval(line)))
    print(n.magnitude())

if '__main__' == __name__:
    main()
