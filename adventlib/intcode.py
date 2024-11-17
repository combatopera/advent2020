class Computer:

    pc = 0

    def __init__(self, data):
        self.data = data

    def opcode1(self):
        self.data[self.data[self.pc + 3]] = self._fetch(1) + self._fetch(2)
        return 4

    def opcode2(self):
        self.data[self.data[self.pc + 3]] = self._fetch(1) * self._fetch(2)
        return 4

    def opcode3(self):
        self.data[self.data[self.pc + 1]] = int(input('Integer: '))
        return 2

    def opcode4(self):
        print(self._fetch(1))
        return 2

    def _fetch(self, off):
        val = self.data[self.pc + off]
        mode = self.modes // (10 ** (off - 1)) % 10
        return val if mode else self.data[val]

    def run(self):
        while True:
            k = self.data[self.pc]
            if 99 == k:
                break
            self.modes, opcode = divmod(k, 100)
            self.pc += getattr(self, f"opcode{opcode}")()
