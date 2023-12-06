from adventlib import inpath
from math import ceil, floor
import re

number = re.compile('[0-9]+')

def roots(a, b, c):
    t = (b ** 2 - 4 * a * c) ** .5
    for s in -1, 1:
        yield (-b + s * t) / (2 * a)

def main():
    with inpath().open() as f:
        time, distance = (int(''.join(number.findall(l))) for l in f)
    '''
    distance < speed * (time - speed)
    speed ** 2 - time * speed + distance < 0
    '''
    lo, hi = roots(1, -time, distance)
    print(ceil(hi) - floor(lo) - 1)
