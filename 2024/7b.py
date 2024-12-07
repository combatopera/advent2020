from adventlib import inpath
from math import floor, log10
import numpy as np, operator

def _cat(x, y):
    return 10 ** (floor(log10(y)) + 1) * x + y

operators = operator.add, operator.mul, _cat

def _check(total, args):
    for x in range(3 ** (len(args) - 1)):
        x = list(map(int, np.base_repr(x, base = 3)))
        x = [0] * (len(args) - 1 - len(x)) + x
        n = args[0]
        for i, a in enumerate(args[1:]):
            n = operators[x[i]](n, a)
        if n == total:
            return True

def main():
    def g():
        for l in inpath().read_text().splitlines():
            total, l = l.split(':')
            total = int(total)
            args = list(map(int, l.split()))
            if _check(total, args):
                yield total
    print(sum(g()))
