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

def _callerpath():
    for x in inspect.stack():
        p = x.frame.f_globals['__file__']
        if p != __file__:
            return Path(p)

def inpath():
    path = _callerpath()
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
    path = _callerpath().parent / f"{taskname}.py"
    exec(f"{path.read_text()}main()", dict(print = capture, __file__ = str(path)))
    return capture.answer

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
