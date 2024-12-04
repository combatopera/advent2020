from itertools import islice
from pathlib import Path
from subprocess import DEVNULL
from tempfile import NamedTemporaryFile
import atexit, inspect, re, sys

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
    from lagoon import gpg
    caller = _callerpath()
    plainpath = caller.parent / 'input' / re.match('[0-9]+', caller.name).group()
    if plainpath.exists():
        print(f"Using plain path: {plainpath}", file = sys.stderr)
        return plainpath
    f = NamedTemporaryFile()
    atexit.register(f.close)
    gpg.__decrypt(f"{plainpath}.gpg", stdout = f, stderr = DEVNULL)
    return Path(f.name)

def readgrid(type = lambda x: x):
    for y, l in enumerate(inpath().read_text().splitlines()):
        for x, c in enumerate(l):
            yield Vector([x, y]), type(c)

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

    @classmethod
    def _of(cls, *args, **kwargs):
        return cls(*args, **kwargs)

    def __add__(self, that):
        return self._of(x + y for x, y in zip(self, that))

    def __sub__(self, that):
        return self._of(x - y for x, y in zip(self, that))

    def __mul__(self, n):
        return self._of(x * n for x in self)

    def __truediv__(self, n):
        return self._of(x / n for x in self)

    def __mod__(self, that):
        return self._of(x % y for x, y in zip(self, that))

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
