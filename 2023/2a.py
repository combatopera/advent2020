from adventlib import inpath
from collections import defaultdict
import re

limits = dict(red = 12, green = 13, blue = 14)

def possible():
    with inpath().open() as f:
        for l in f:
            bounds = defaultdict(int)
            game, fetches = l.rstrip().split(': ')
            for fetch in fetches.split('; '):
                for color in fetch.split(', '):
                    n, c = color.split(' ')
                    bounds[c] = max(bounds[c], int(n))
            if all(bounds[c] <= limits[c] for c in limits):
                yield int(game.split()[1])

def main():
    print(sum(possible()))
