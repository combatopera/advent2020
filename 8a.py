#!/usr/bin/env python3

from pathlib import Path

class Program:

    def __init__(self, f):
        def g():
            for line in f:
                yield [t(w) for t, w in zip([str, int], line.split(' '))]
        self.instructions = list(g())

class Computer:

    accumulator = 0
    pc = 0

    def run(self, program):
        visited = set()
        while self.pc not in visited:
            name, arg = program.instructions[self.pc]
            getattr(self, name)(arg)
            visited.add(self.pc)
            self.pc += 1

    def acc(self, arg):
        self.accumulator += arg

    def jmp(self, arg):
        self.pc += arg - 1

    def nop(self, arg):
        pass

def main():
    with Path('input', '8').open() as f:
        program = Program(f)
    c = Computer()
    c.run(program)
    print(c.accumulator)

if '__main__' == __name__:
    main()
