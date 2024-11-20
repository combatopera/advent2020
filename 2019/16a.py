from adventlib import inpath

def _positive(outno, size):
    i = outno - 1
    while i < size:
        yield range(i, min(i + outno, size))
        i += outno * 4

def _negative(outno, size):
    i = 3 * outno - 1
    while i < size:
        yield range(i, min(i + outno, size))
        i += outno * 4

def main():
    def fft():
        for outno in range(1, size + 1):
            yield abs(sum(signal[i] for r in _positive(outno, size) for i in r) - sum(signal[i] for r in _negative(outno, size) for i in r)) % 10
    signal = list(map(int, inpath().read_text().rstrip()))
    size = len(signal)
    for _ in range(100):
        signal = list(fft())
    print(''.join(map(str, signal[:8])))
