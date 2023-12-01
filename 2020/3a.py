from pathlib import Path

slope = 3, 1

class Map:

    def __init__(self, rows):
        self.w = len(rows[0])
        self.rows = rows

    def tree(self, x, y):
        return '#' == self.rows[y][x % self.w]

def main():
    m = Map(Path('input', '3').read_text().splitlines())
    xy = [0, 0]
    trees = 0
    try:
        while True:
            for i in range(2):
                xy[i] += slope[i]
            trees += m.tree(*xy)
    except IndexError:
        print(trees)
