from adventlib import inpath
from functools import reduce
import operator, re

number = re.compile('[0-9]+')

def main():
    def ways(t, d):
        def distances():
            for speed in range(t + 1):
                yield speed * (t - speed)
        return sum(1 for x in distances() if x > d)
    with inpath().open() as f:
        times, distances = (list(map(int, number.findall(l))) for l in f)
    print(reduce(operator.mul, (ways(*v) for v in zip(times, distances))))
