from adventlib import inpath

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
            self.cursor += 4

def main():
    program = [int(s) for s in inpath().read_text().split(',')]
    program[1] = 12
    program[2] = 2
    Computer(program).run()
    print(program[0])
