from adventlib import inpath
from itertools import islice

base = 0, 1, 0, -1

def _pattern(i):
    while True:
        for x in base:
            for _ in range(1 + i):
                yield x

def main():
    def fft():
        for i in range(n):
            yield abs(sum(x * k for x, k in zip(signal, islice(_pattern(i), 1, None)))) % 10
    signal = list(map(int, inpath().read_text().rstrip()))
    n = len(signal)
    for _ in range(100):
        signal = list(fft())
    print(''.join(map(str, signal[:8])))
