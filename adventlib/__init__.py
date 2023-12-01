from itertools import islice
from pathlib import Path
import inspect, re

def readchunks(f):
    def g():
        for l in f:
            yield l.rstrip()
        yield ''
    chunk = []
    for l in g():
        if l:
            chunk.append(l)
        elif chunk:
            yield chunk.copy()
            chunk.clear()

class SeatReader:

    xform = dict(F = 0, B = 1, L = 0, R = 1)

    def __init__(self, width):
        self.factors = [2 ** i for i in range(width)]
        self.factors.reverse()

    def read(self, f):
        for l in f:
            yield sum(f * self.xform[l[i]] for i, f in enumerate(self.factors))

def _callerpath(stack):
    return Path(stack[1].frame.f_globals['__file__'])

def inpath():
    path = _callerpath(inspect.stack())
    return path.parent / 'input' / re.match('[0-9]+', path.name).group()

def answerof(taskname):
    'Pretend we saved it.'
    class Capture:
        def __call__(self, answer):
            try:
                self.answer
            except AttributeError:
                self.answer = answer
            else:
                raise Exception
    capture = Capture()
    exec(f"""{(_callerpath(inspect.stack()).parent / f"{taskname}.py").read_text()}main()""", dict(print = capture))
    return capture.answer

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

def differentiate(v):
    return [y - x for x, y in zip(v, islice(v, 1, None))]

class Vector(tuple):

    def __add__(self, that):
        return type(self)(x + y for x, y in zip(self, that))

    def __sub__(self, that):
        return type(self)(x - y for x, y in zip(self, that))

    def __truediv__(self, n):
        return type(self)(x / n for x in self)

    def __mod__(self, that):
        return type(self)(x % y for x, y in zip(self, that))

    def maxhattan(self):
        return max(map(abs, self))

    def manhattan(self):
        return sum(map(abs, self))

    def diagonal(self):
        return sum(map(bool, self)) > 1

def intsin(k):
    return (k & 1) * (1 - (k // 2) * 2)

def intcos(k):
    return intsin(k + 1)
