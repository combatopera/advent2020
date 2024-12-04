from adventlib import readgrid, Vector

X = [Vector((x, y)) for x in [-1, 1] for y in [-1, 1]]
MS = set('MS')

def main():
    n = 0
    grid = dict(readgrid())
    for p, c in grid.items():
        if 'A' == c:
            if all(MS == {grid.get(p + d * i) for i in [-1, 1]} for d in X):
                n += 1
    print(n)
