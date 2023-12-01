from itertools import islice
from adventlib import inpath

def main():
    print(sum(1 for v in [list(map(int, inpath().read_text().splitlines()))] for x, y in zip(v, islice(v, 1, None)) if x < y))
