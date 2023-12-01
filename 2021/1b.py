from adventlib import inpath
from itertools import islice

def main():
    v = list(map(int, inpath().read_text().splitlines()))
    w = sum(islice(v, 3))
    n = 0
    for x, y in zip(v, islice(v, 3, None)):
        w_ = w - x + y
        n += w < w_
        w = w_
    print(n)
