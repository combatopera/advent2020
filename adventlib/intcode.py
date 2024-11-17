class Computer:

    pc = 0

    def __init__(self, data, inputs = None):
        self.data = data
        self.inputs = inputs

    def opcode1(self):
        self._store(3, self._fetch(1) + self._fetch(2))
        return 4

    def opcode2(self):
        self._store(3, self._fetch(1) * self._fetch(2))
        return 4

    def opcode3(self):
        self._store(1, self.inputs.pop(0))
        return 2

    def opcode4(self):
        print(self._fetch(1))
        return 2

    def opcode5(self):
        return self._fetch(2) - self.pc if self._fetch(1) else 3

    def opcode6(self):
        return 3 if self._fetch(1) else self._fetch(2) - self.pc

    def opcode7(self):
        self._store(3, self._fetch(1) < self._fetch(2))
        return 4

    def opcode8(self):
        self._store(3, self._fetch(1) == self._fetch(2))
        return 4

    def _fetch(self, off):
        val = self.data[self.pc + off]
        mode = self.modes // (10 ** (off - 1)) % 10
        return val if mode else self.data[val]

    def _store(self, off, value):
        self.data[self.data[self.pc + off]] = value

    def run(self):
        while True:
            k = self.data[self.pc]
            if 99 == k:
                break
            self.modes, opcode = divmod(k, 100)
            self.pc += getattr(self, f"opcode{opcode}")()
