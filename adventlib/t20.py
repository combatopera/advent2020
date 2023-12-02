import re

class SeatReader:

    xform = dict(F = 0, B = 1, L = 0, R = 1)

    def __init__(self, width):
        self.factors = [2 ** i for i in range(width)]
        self.factors.reverse()

    def read(self, f):
        for l in f:
            yield sum(f * self.xform[l[i]] for i, f in enumerate(self.factors))

class BagRule:

    outer = re.compile('(.+) bags contain (.+)[.]')
    inner = re.compile('([1-9]) (.+) bags?')

    @classmethod
    def readmany(cls, f):
        for l in f:
            yield cls(l.rstrip())

    def __init__(self, line):
        self.lhs, v = self.outer.fullmatch(line).groups()
        self.rhs = {} if 'no other bags' == v else {c: int(n) for x in v.split(', ') for n, c in [self.inner.fullmatch(x).groups()]}

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
