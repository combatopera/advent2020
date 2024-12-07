from adventlib import inpath
import operator

def _check(total, args):
    for x in range(1 << (len(args) - 1)):
        n = args[0]
        for i, a in enumerate(args[1:]):
            n = (operator.mul if x & (1 << i) else operator.add)(n, a)
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
