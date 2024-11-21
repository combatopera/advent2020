from adventlib import inpath, Vector
from adventlib.intcode import Computer

plus = (-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)
dirs = (0, -1), (1, 0), (0, 1), (-1, 0)

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
            grid[x, y] = c = chr(k)
            try:
                direction = '^>v<'.index(c)
            except ValueError:
                pass
            else:
                robot = Vector([x, y])
            x += 1
    h = y
    #for y in range(h):
    #    print(''.join(grid[x, y] for x in range(w)))
    program = []
    while True:
        if '#' == grid.get(robot + dirs[(direction - 1) % 4]):
            program.append('L')
            direction = (direction - 1) % 4
        elif '#' == grid[robot + dirs[(direction + 1) % 4]]:
            program.append('R')
            direction = (direction + 1) % 4
        else:
            break
        n = 0
        while '#' == grid.get(robot + dirs[direction]):
            n += 1
            robot += dirs[direction]
        program.append(n)
    for x, y in zip(program[::2], program[1::2]): print(x, y)
