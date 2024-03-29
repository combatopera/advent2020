from adventlib import inpath
import re

pattern = re.compile('([0-9]+)-([0-9]+) (.): (.+)')

def main():
    v = [pattern.fullmatch(l).groups() for l in inpath().read_text().splitlines()]
    valid = 0
    for *positions, c, p in v:
        indices = [int(s) - 1 for s in positions]
        valid += 1 == sum(p[i] == c for i in indices)
    print(valid)
