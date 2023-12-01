from adventlib import inpath
import re

pattern = re.compile('([0-9]+)-([0-9]+) (.): (.+)')

def main():
    v = [pattern.fullmatch(l).groups() for l in inpath().read_text().splitlines()]
    valid = 0
    for m, n, c, p in v:
        m, n = map(int, [m, n])
        k = p.count(c)
        valid += m <= k and k <= n
    print(valid)
