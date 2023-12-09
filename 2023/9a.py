from adventlib import inpath, differentiate
import re

def extrapolate(v):
    derivatives = [v]
    while any(derivatives[-1]):
        derivatives.append(differentiate(derivatives[-1]))
    return sum(d[-1] for d in derivatives)

def main():
    def g():
        with inpath().open() as f:
            for l in f:
                yield extrapolate(list(map(int, re.findall('[0-9-]+', l))))
    print(sum(g()))
