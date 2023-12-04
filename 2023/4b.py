from adventlib import inpath
from collections import defaultdict
import re

number = re.compile('[0-9]+')

def main():
    copies = defaultdict(int)
    with inpath().open() as f:
        for i, l in enumerate(f):
            copies[i] += 1
            _, l = l.split(': ')
            l, r = l.split(' | ')
            win = set(number.findall(l))
            for j in range(sum(1 for x in number.findall(r) if x in win)):
                copies[i + 1 + j] += copies[i]
    print(sum(copies.values()))
