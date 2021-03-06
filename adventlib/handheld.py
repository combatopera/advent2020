class Program:

    @classmethod
    def load(cls, f):
        def g():
            for line in f:
                yield [t(w) for t, w in zip([str, int], line.split(' '))]
        return cls(list(g()))

    def __init__(self, instructions):
        self.instructions = instructions

    def patched(self, i, name):
        instructions = self.instructions.copy()
        instructions[i] = [name, *instructions[i][1:]]
        return type(self)(instructions)

class Computer:

    def exec(self, program):
        self.accumulator = 0
        self.pc = 0
        visited = set()
        while self.pc not in visited:
            try:
                name, arg = program.instructions[self.pc]
            except IndexError:
                return True
            visited.add(self.pc)
            getattr(self, name)(arg)
            self.pc += 1

    def acc(self, arg):
        self.accumulator += arg

    def jmp(self, arg):
        self.pc += arg - 1

    def nop(self, arg):
        pass
