class Computer:

    cursor = 0

    def __init__(self, program):
        self.program = program

    def opcode1(self):
        self.program[self.program[self.cursor + 3]] = self.program[self.program[self.cursor + 1]] + self.program[self.program[self.cursor + 2]]
        return 4

    def opcode2(self):
        self.program[self.program[self.cursor + 3]] = self.program[self.program[self.cursor + 1]] * self.program[self.program[self.cursor + 2]]
        return 4

    def run(self):
        while True:
            opcode = self.program[self.cursor]
            if 99 == opcode:
                break
            self.cursor += getattr(self, f"opcode{opcode}")()
