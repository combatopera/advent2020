from functools import reduce
from pathlib import Path
import operator

slopes = (
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2],
)

class Map:

    def __init__(self, rows):
        self.w = len(rows[0])
        self.rows = rows

    def tree(self, x, y):
        return '#' == self.rows[y][x % self.w]

    def trees(self, slope):
        xy = [0, 0]
        trees = 0
        try:
            while True:
                for i in range(2):
                    xy[i] += slope[i]
                trees += self.tree(*xy)
        except IndexError:
            return trees

def main():
    m = Map(Path('input', '3').read_text().splitlines())
    print(reduce(operator.mul, map(m.trees, slopes)))
