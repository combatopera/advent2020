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
    v = list(map(int, inpath().read_text().split()))
    for _ in range(25):
        v = list(blink(v))
    print(len(v))
