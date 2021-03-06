#!/usr/bin/env python3

from functools import reduce
from pathlib import Path
import operator

def intceil(x, y):
    return -(x // -y)

def main():
    with Path('input', '13').open() as f:
        seaport, buses = f
    seaport = int(seaport)
    buses = [int(b) for b in buses.split(',') if 'x' != b]
    print(reduce(operator.mul, min((intceil(seaport, b) * b - seaport, b) for b in buses)))

if '__main__' == __name__:
    main()
