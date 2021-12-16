#!/usr/bin/env python3

from functools import reduce
from operator import eq, gt, lt, mul
from pathlib import Path
from types import SimpleNamespace

literaltype = 4

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
        while part & 0x10:
            part = self._read(5)
            k = (k << 4) | part & 0xf
        return k

    def _packet(self):
        version = self._read(3)
        type = self._read(3)
        if literaltype == type:
            payload = self._readliteral()
        else:
            if self._read(1):
                count = self._read(11)
                payload = [self._packet() for _ in range(count)]
            else:
                stop = self._read(15) + self.i
                payload = []
                while self.i != stop:
                    payload.append(self._packet())
        return Packet(version = version, type = type, payload = payload)

    def packet(self):
        while self.i % 4:
            self.i += 1
        if any(self.bits[self.i:]):
            return self._packet()

class Packet(SimpleNamespace):

    def versions(self):
        yield self.version
        if literaltype != self.type:
            for p in self.payload:
                yield from p.versions()

    def calc(self):
        if 0 == self.type:
            return sum(p.calc() for p in self.payload)
        if 1 == self.type:
            return reduce(mul, (p.calc() for p in self.payload))
        if 2 == self.type:
            return min(p.calc() for p in self.payload)
        if 3 == self.type:
            return max(p.calc() for p in self.payload)
        if 4 == self.type:
            return self.payload
        if 5 == self.type:
            return gt(*(p.calc() for p in self.payload))
        if 6 == self.type:
            return lt(*(p.calc() for p in self.payload))
        if 7 == self.type:
            return eq(*(p.calc() for p in self.payload))




def main():
    text = Path('input', '16').read_text().rstrip()
    cursor = Cursor([(i >> b) & 1 for c in text for i in [int(c, 16)] for b in range(3, -1, -1)])
    print(cursor.packet().calc())

if '__main__' == __name__:
    main()
