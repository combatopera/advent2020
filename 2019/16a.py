from adventlib import inpath
from itertools import islice

base = 0, 1, 0, -1

def _pattern(i, n):
    def g():
        while True:
            for x in base:
                for _ in range(1 + i):
                    yield x
    return list(islice(g(), 1, n + 1))

def main():
    def fft():
        for p in patterns:
            yield abs(sum(x * k for x, k in zip(signal, p))) % 10
    signal = list(map(int, inpath().read_text().rstrip()))
    n = len(signal)
    patterns = [_pattern(i, n) for i in range(n)]
    for _ in range(100):
        signal = list(fft())
    print(''.join(map(str, signal[:8])))
