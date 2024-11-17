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

    def opcode3(self):
        self.program[self.program[self.cursor + 1]] = int(input('Integer: '))
        return 2

    def opcode4(self):
        print(self.program[self.program[self.cursor + 1]])
        return 2

    def run(self):
        while True:
            k = self.program[self.cursor]
            opcode = k % 100
            if 99 == opcode:
                break
            self.cursor += getattr(self, f"opcode{opcode}")()
