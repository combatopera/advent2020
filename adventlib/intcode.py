from collections import defaultdict

class Computer:

    relbase = pc = 0

    def __init__(self, data, inputs = None):
        self.data = defaultdict(int)
        for i, x in enumerate(data):
            self.data[i] = x
        self.inputs = inputs

    def opcode1(self):
        self._store(3, self._fetch(1) + self._fetch(2))
        self.pc += 4

    def opcode2(self):
        self._store(3, self._fetch(1) * self._fetch(2))
        self.pc += 4

    def opcode3(self):
        self._store(1, self.inputs.pop(0))
        self.pc += 2

    def opcode4(self):
        yield self._fetch(1)
        self.pc += 2

    def opcode5(self):
        self.pc = self._fetch(2) if self._fetch(1) else self.pc + 3

    def opcode6(self):
        self.pc = self.pc + 3 if self._fetch(1) else self._fetch(2)

    def opcode7(self):
        self._store(3, self._fetch(1) < self._fetch(2))
        self.pc += 4

    def opcode8(self):
        self._store(3, self._fetch(1) == self._fetch(2))
        self.pc += 4

    def opcode9(self):
        self.relbase += self._fetch(1)
        self.pc += 2

    def _fetch(self, off):
        return getattr(self, f"fetch{self.modes // (10 ** (off - 1)) % 10}")(self.data[self.pc + off])

    def fetch0(self, val):
        return self.data[val]

    def fetch1(self, val):
        return val

    def fetch2(self, val):
        return self.data[self.relbase + val]

    def _store(self, off, value):
        self.data[self.data[self.pc + off]] = value

    def __iter__(self):
        while True:
            k = self.data[self.pc]
            if 99 == k:
                break
            self.modes, opcode = divmod(k, 100)
            g = getattr(self, f"opcode{opcode}")()
            if g is not None:
                yield from g

    def run(self):
        for x in self:
            print(x)
