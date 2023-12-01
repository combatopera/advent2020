from functools import reduce
from adventlib import inpath
import operator

def intceil(x, y):
    return -(x // -y)

def main():
    with inpath().open() as f:
        seaport, buses = f
    seaport = int(seaport)
    buses = [int(b) for b in buses.split(',') if 'x' != b]
    print(reduce(operator.mul, min((intceil(seaport, b) * b - seaport, b) for b in buses)))
