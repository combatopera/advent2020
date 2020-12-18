#!/usr/bin/env python3

from itertools import islice
from pathlib import Path
import operator, re

ops = {'+': operator.add, '*': operator.mul}
token = re.compile('([0-9]+)|([+*])')

def split(text):
    for n, op in token.findall(text):
        yield int(n) if n else ops[op]

def find(text, c, start):
    i = text.find(c, start)
    return i if -1 != i else len(text)

class Expr:

    @classmethod
    def _parse(cls, text, cursor):
        v = []
        while True:
            open = find(text, '(', cursor)
            close = find(text, ')', cursor)
            if open < close:
                v.extend(split(text[cursor:open]))
                w, cursor = cls._parse(text, open + 1)
                v.append(w)
            else:
                v.extend(split(text[cursor:close]))
                return cls(v), close + 1

    @classmethod
    def parse(cls, text):
        return cls._parse(text, 0)[0]

    def __init__(self, expr):
        self.expr = expr

    def eval(self):
        def eval(e):
            try:
                return e.eval()
            except AttributeError:
                return e
        acc = eval(self.expr[0])
        for op, expr in zip(islice(self.expr, 1, None, 2), islice(self.expr, 2, None, 2)):
            acc = op(acc, eval(expr))
        return acc

def main():
    def g():
        with Path('input', '18').open() as f:
            for l in f:
                yield Expr.parse(l).eval()
    print(sum(g()))

if '__main__' == __name__:
    main()
