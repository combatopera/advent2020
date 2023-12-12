from adventlib import inpath
from functools import lru_cache
from itertools import islice

def charat(text, i):
    return text[i] if i >= 0 and i < len(text) else '.'

@lru_cache(None)
def ways(text, j, v, i):
    if i == len(v):
        return all('#' != text[k] for k in range(j, len(text)))
    w = v[i]
    maxj = len(text) - (sum(islice(v, i, None)) + len(v) - i - 1)
    n = 0
    while j <= maxj and '#' != charat(text, j - 1):
        if '#' != charat(text, j + w) and all('.' != text[k] for k in range(j, j + w)):
            n += ways(text, j + w + 1, v, i + 1)
        j += 1
    return n

def main():
    def g():
        with inpath().open() as f:
            for l in f:
                u, v = l.split()
                yield ways('?'.join(u for _ in range(mul)), 0, tuple(map(int, v.split(','))) * mul, 0)
    mul = 5
    print(sum(g()))
