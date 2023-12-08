from adventlib import inpath, readchunks
from functools import reduce
import operator, re

def main():
    with inpath().open() as f:
        (top,), rest = readchunks(f)
    chart = {k: dict(L = l, R = r) for line in rest for k, l, r in [re.findall('[A-Z]{3}', line)]}
    def g():
        for key in chart:
            if 'A' == key[-1]:
                times = 0
                while 'Z' != key[-1]:
                    for c in top:
                        key = chart[key][c]
                    times += 1
                yield times
    print(reduce(operator.mul, g()) * len(top))
