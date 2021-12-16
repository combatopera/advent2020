#!/usr/bin/env python3

from pathlib import Path

class Computer:

    cursor = 0

    def __init__(self, program):
        self.program = program

    def run(self):
        while True:
            k = self.program[self.cursor]
            if 99 == k:
                break
            if 1 == k:
                self.program[self.program[self.cursor + 3]] = self.program[self.program[self.cursor + 1]] + self.program[self.program[self.cursor + 2]]
            elif 2 == k:
                self.program[self.program[self.cursor + 3]] = self.program[self.program[self.cursor + 1]] * self.program[self.program[self.cursor + 2]]
            else:
                panic
            self.cursor += 4

def main():
    program = [int(s) for s in Path('input', '2').read_text().split(',')]
    for noun in range(100):
        for verb in range(100):
            p = program.copy()
            p[1] = noun
            p[2] = verb
            Computer(p).run()
            if 19690720 == p[0]:
                print(100 * noun + verb)
                return

if '__main__' == __name__:
    main()
