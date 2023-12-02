from adventlib import inpath
from collections import defaultdict
from functools import reduce
import operator

def powers():
    with inpath().open() as f:
        for l in f:
            bounds = dict(red = 0, green = 0, blue = 0)
            game, fetches = l.rstrip().split(': ')
            for fetch in fetches.split('; '):
                for color in fetch.split(', '):
                    n, c = color.split(' ')
                    bounds[c] = max(bounds[c], int(n))
            yield reduce(operator.mul, bounds.values())

def main():
    print(sum(powers()))
