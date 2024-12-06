from adventlib import readgrid

dirs = (0, -1), (1, 0), (0, 1), (-1, 0)

def main():
    grid = {}
    for p, c in readgrid():
        grid[p] = c
        if '^' == c:
            guard = p
            d = 0
    footprint = {guard}
    while True:
        p = guard + dirs[d]
        c = grid.get(p)
        if c is None:
            break
        if '#' == c:
            d = (d + 1) % len(dirs)
        else:
            guard = p
            footprint.add(p)
    print(len(footprint))
