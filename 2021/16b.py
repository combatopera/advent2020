from functools import reduce
from operator import eq, gt, lt, mul
from pathlib import Path
from types import SimpleNamespace

literaltype = 4
mask = 0x10

class Cursor:

    i = 0

    def __init__(self, bits):
        self.bits = bits

    def _read(self, n):
        k = 0
        for _ in range(n):
            k = (k << 1) | self.bits[self.i]
            self.i += 1
        return k

    def _readliteral(self):
        k = 0
        part = -1
        while part & mask:
            part = self._read(5)
            k = (k << 4) | part & ~mask
        return k

    def packet(self):
        version = self._read(3)
        type = self._read(3)
        if literaltype == type:
            payload = self._readliteral()
        else:
            if self._read(1):
                count = self._read(11)
                payload = [self.packet() for _ in range(count)]
            else:
                stop = self._read(15) + self.i
                payload = []
                while self.i != stop:
                    payload.append(self.packet())
        return Packet(version = version, type = type, payload = payload)

class Packet(SimpleNamespace):

    ops = {
        0: sum,
        1: lambda v: reduce(mul, v),
        2: min,
        3: max,
        5: lambda v: gt(*v),
        6: lambda v: lt(*v),
        7: lambda v: eq(*v),
    }

    def calc(self):
        return self.payload if literaltype == self.type else self.ops[self.type](p.calc() for p in self.payload)

def main():
    text = Path('input', '16').read_text().rstrip()
    cursor = Cursor([(i >> b) & 1 for c in text for i in [int(c, 16)] for b in range(3, -1, -1)])
    print(cursor.packet().calc())
