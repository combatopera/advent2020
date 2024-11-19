from adventlib import inpath
from adventlib.intcode import Computer

def main():
    grid = {}
    i = iter(Computer([int(s) for s in inpath().read_text().split(',')]))
    while True:
        try:
            x = next(i)
        except StopIteration:
            break
        y = next(i)
        tid = next(i)
        grid[x, y] = tid
    print(sum(1 for tid in grid.values() if 2 == tid))
