from adventlib import inpath, readchunks
import re

caps = re.compile('[A-Z]{3}')

def main():
    with inpath().open() as f:
        (top,), rest = readchunks(f)
    chart = {k: dict(L = l, R = r) for line in rest for k, l, r in [caps.findall(line)]}
    steps = 0
    key = 'AAA'
    while 'ZZZ' != key:
        for c in top:
            key = chart[key][c]
        steps += len(top)
    print(steps)
