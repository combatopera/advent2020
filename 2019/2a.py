from adventlib import inpath
from adventlib.intcode import Computer

def main():
    program = [int(s) for s in inpath().read_text().split(',')]
    program[1] = 12
    program[2] = 2
    Computer(program).run()
    print(program[0])
