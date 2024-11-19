from adventlib import inpath
from adventlib.intcode import Computer

class Joystick:

    def pop(self, i):
        assert not i
        if self.ballx < self.paddlex:
            return -1
        if self.paddlex < self.ballx:
            return 1
        return 0

def main():
    program = [int(s) for s in inpath().read_text().split(',')]
    program[0] = 2
    grid = {}
    joystick = Joystick()
    i = iter(Computer(program, joystick))
    while True:
        try:
            x = next(i)
        except StopIteration:
            break
        y = next(i)
        grid[x, y] = arg = next(i)
        if (-1, 0) == (x, y) and all(2 != v for v in grid.values()):
            break
        if 3 == arg:
            joystick.paddlex = x
        elif 4 == arg:
            joystick.ballx = x
    print(grid[-1, 0])
