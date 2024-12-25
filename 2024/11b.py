from adventlib import inpath

def blink(v):
    for x in v:
        if not x:
            yield 1
            continue
        s = str(x)
        if not len(s) & 1:
            i = len(s) // 2
            yield int(s[:i])
            yield int(s[i:])
            continue
        yield 2024 * x

def main():
    n = 0
    for x in map(int, inpath().read_text().split()):
        v = [x]
        for _ in range(25):
            v = list(blink(v))
        n += len(v)
    print(n)
