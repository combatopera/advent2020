from adventlib import inpath

def _positive(i, n):
    i += 1
    k = i - 1
    while k < n:
        yield range(k, min(k + i, n))
        k += i * 4

def _negative(i, n):
    i += 1
    k = 3 * i - 1
    while k < n:
        yield range(k, min(k + i, n))
        k += i * 4

def main():
    def fft():
        for i in range(n):
            yield abs(sum(signal[k] for r in _positive(i, n) for k in r) - sum(signal[k] for r in _negative(i, n) for k in r)) % 10
    signal = list(map(int, inpath().read_text().rstrip()))
    n = len(signal)
    for _ in range(100):
        signal = list(fft())
    print(''.join(map(str, signal[:8])))
