from adventlib import inpath, Vector
from adventlib.intcode import Computer
from collections import defaultdict

dirs = [0, 1], [1, 0], [0, -1], [-1, 0]

def main():
    grid = defaultdict(int)
    position = Vector([0, 0])
    dirindex = 0
    c = Computer([int(s) for s in inpath().read_text().split(',')], [])
    i = iter(c)
    while True:
        c.inputs.append(grid[position])
        try:
            grid[position] = next(i)
        except StopIteration:
            break
        dirindex = (dirindex + next(i) * 2 - 1) % 4
        position += dirs[dirindex]
    print(len(grid))
