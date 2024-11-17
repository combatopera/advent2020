from adventlib import inpath
from adventlib.intcode import Computer

def main():
    program = [int(s) for s in inpath().read_text().split(',')]
    Computer(program).run()
