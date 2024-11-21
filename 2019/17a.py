from adventlib import inpath, Vector
from adventlib.intcode import Computer

plus = (-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)

def main():
    grid = {}
    x = y = 0
    for k in Computer(map(int, inpath().read_text().split(','))):
        if 10 == k:
            if x:
                w = x
                x = 0
                y += 1
        else:
            grid[x, y] = chr(k)
            x += 1
    h = y
    def g():
        for y in range(1, h - 1):
            for x in range(1, w - 1):
                if all('#' == grid[Vector([x, y]) + off] for off in plus):
                    yield x * y
    print(sum(g()))
