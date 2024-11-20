from adventlib import inpath

class Size:

    def __init__(self, n):
        self.n = n

    def _ranges(self, w, i):
        while i < self.n:
            yield range(i, min(i + w, self.n))
            i += w * 4

    def positive(self, j):
        return self._ranges(j + 1, j)

    def negative(self, j):
        return self._ranges(j + 1, 3 * j + 2)

def main():
    def fft():
        for j in range(size.n):
            yield abs(sum(signal[i] for r in size.positive(j) for i in r) - sum(signal[i] for r in size.negative(j) for i in r)) % 10
    signal = list(map(int, inpath().read_text().rstrip()))
    size = Size(len(signal))
    for _ in range(100):
        signal = list(fft())
    print(''.join(map(str, signal[:8])))
