from adventlib import inpath
from itertools import combinations
import re

class Record:

    def __init__(self, text):
        self.hashes = sum(1 for c in text if '#' == c)
        self.holes = [i for i, c in enumerate(text) if '?' == c]
        self.text = text

    def options(self, check):
        hashes = sum(check) - self.hashes
        for indices in combinations(self.holes, hashes):
            v = list(self.text)
            for i in indices:
                v[i] = '#'
            if list(map(len, re.findall('#+', ''.join(v)))) == check:
                yield

def main():
    def g():
        with inpath().open() as f:
            for l in f:
                u, v = l.split()
                record = Record('?'.join(u for _ in range(5)))
                check = list(map(int, v.split(','))) * 5
                n = sum(1 for _ in record.options(check))
                yield n
    print(sum(g()))
