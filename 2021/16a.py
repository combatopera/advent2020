from adventlib import inpath
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

    def versions(self):
        yield self.version
        if literaltype != self.type:
            for p in self.payload:
                yield from p.versions()

def main():
    text = inpath().read_text().rstrip()
    cursor = Cursor([(i >> b) & 1 for c in text for i in [int(c, 16)] for b in range(3, -1, -1)])
    print(sum(cursor.packet().versions()))
