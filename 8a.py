#!/usr/bin/env python3

from pathlib import Path

class Program:

    def __init__(self, f):
        def g():
            for line in f:
                yield [t(w) for t, w in zip([str, int], line.split(' '))]
        self.instructions = list(g())

class Execution:

    accumulator = 0
    pc = 0

    def __init__(self, program):
        visited = set()
        while self.pc not in visited:
            visited.add(self.pc)
            name, arg = program.instructions[self.pc]
            getattr(self, name)(arg)
            self.pc += 1

    def acc(self, arg):
        self.accumulator += arg

    def jmp(self, arg):
        self.pc += arg - 1

    def nop(self, arg):
        pass

def main():
    with Path('input', '8').open() as f:
        print(Execution(Program(f)).accumulator)

if '__main__' == __name__:
    main()
