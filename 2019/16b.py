from adventlib import inpath

def main():
    line = inpath().read_text().rstrip()
    signal = (list(map(int, line)) * 10000)[int(line[:7]):]
    n = len(signal)
    for _ in range(100):
        def g():
            total = 0
            for j in range(n)[::-1]:
                total += signal[j]
                yield abs(total) % 10
        signal = list(g())
        signal.reverse()
    print(''.join(map(str, signal[:8])))
