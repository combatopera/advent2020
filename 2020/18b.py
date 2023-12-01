from functools import reduce
from itertools import islice
from pathlib import Path
import operator, re

ops = {'+': operator.add, '*': operator.mul}
token = re.compile('([0-9]+)|([+*])')

def split(text):
    for n, op in token.findall(text):
        yield Int(n) if n else ops[op]

def find(text, c, start):
    i = text.find(c, start)
    return i if -1 != i else len(text)

class Int(int):

    def eval(self):
        return self

class Expr:

    @classmethod
    def _parse(cls, text, cursor):
        v = []
        while True:
            b = min(find(text, c, cursor) for c in '()')
            v.extend(split(text[cursor:b]))
            if b < len(text) and '(' == text[b]:
                w, cursor = cls._parse(text, b + 1)
                v.append(w)
            else:
                return cls(v), b + 1

    @classmethod
    def parse(cls, text):
        return cls._parse(text, 0)[0]

    def __init__(self, expr):
        self.expr = expr

    def evalsimple(self):
        acc = self.expr[0].eval()
        for op, expr in zip(islice(self.expr, 1, None, 2), islice(self.expr, 2, None, 2)):
            acc = op(acc, expr.eval())
        return acc

    def eval(self):
        def sums():
            i = 0
            try:
                while True:
                    j = self.expr.index(operator.mul, i)
                    yield self.expr[i:j]
                    i = j + 1
            except ValueError:
                yield self.expr[i:]
        return reduce(operator.mul, (Expr(s).evalsimple() for s in sums()))

def main():
    def g():
        with Path('input', '18').open() as f:
            for l in f:
                yield Expr.parse(l).eval()
    print(sum(g()))
