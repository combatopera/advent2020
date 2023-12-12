from adventlib import inpath
from itertools import islice

def charat(text, i):
    return text[i] if i >= 0 and i < len(text) else '.'

def fit(v, i, text, j):
    if i == len(v):
        yield ()
    else:
        w = v[i]
        maxj = len(text) - (sum(islice(v, i, None)) + len(v) - i - 1)
        while j <= maxj and '#' != charat(text, j - 1):
            if '#' != charat(text, j + w) and all('.' != text[k] for k in range(j, j + w)):
                for more in fit(v, i + 1, text, j + w + 1):
                    yield [j, *more]
            j += 1

def main():
    def g():
        with inpath().open() as f:
            for l in f:
                record, v = l.split()
                record = '?'.join(record for _ in range(mul))
                check = list(map(int, v.split(','))) * mul
                yield sum(1 for _ in fit(check, 0, record, 0))
    mul = 5
    print(sum(g()))
