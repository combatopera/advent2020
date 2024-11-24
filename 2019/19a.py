from adventlib import inpath
from adventlib.intcode import Computer

def main():
    program = list(map(int, inpath().read_text().split(',')))
    print(sum(next(iter(Computer(program, [x, y]))) for y in range(50) for x in range(50)))
