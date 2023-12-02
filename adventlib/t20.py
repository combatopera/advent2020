import re

class SeatReader:

    xform = dict(F = 0, B = 1, L = 0, R = 1)

    def __init__(self, width):
        self.factors = [2 ** i for i in range(width)]
        self.factors.reverse()

    def read(self, f):
        for l in f:
            yield sum(f * self.xform[l[i]] for i, f in enumerate(self.factors))

class BagRule:

    outer = re.compile('(.+) bags contain (.+)[.]')
    inner = re.compile('([1-9]) (.+) bags?')

    @classmethod
    def readmany(cls, f):
        for l in f:
            yield cls(l.rstrip())

    def __init__(self, line):
        self.lhs, v = self.outer.fullmatch(line).groups()
        self.rhs = {} if 'no other bags' == v else {c: int(n) for x in v.split(', ') for n, c in [self.inner.fullmatch(x).groups()]}
