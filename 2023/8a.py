from adventlib import inpath, readchunks
import re

def main():
    with inpath().open() as f:
        (top,), rest = readchunks(f)
    chart = {k: dict(L = l, R = r) for line in rest for k, l, r in [re.findall('[A-Z]{3}', line)]}
    times = 0
    key = 'AAA'
    while 'ZZZ' != key:
        for c in top:
            key = chart[key][c]
        times += 1
    print(times * len(top))
