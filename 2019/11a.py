from adventlib import inpath, Ring, Vector
from adventlib.intcode import Computer
from collections import defaultdict

def main():
    grid = defaultdict(int)
    position = Vector([0, 0])
    dirs = Ring([[0, -1], [1, 0], [0, 1], [-1, 0]])
    c = Computer([int(s) for s in inpath().read_text().split(',')], [])
    i = iter(c)
    while True:
        c.inputs.append(grid[position])
        try:
            grid[position] = next(i)
        except StopIteration:
            break
        position += dirs.iadd(next(i) * 2 - 1)[0]
    print(len(grid))
