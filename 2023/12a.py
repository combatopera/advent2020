from adventlib import inpath
from itertools import combinations
import re

class Record:

    def __init__(self, text):
        self.hashes = sum(1 for c in text if '#' == c)
        self.holes = [i for i, c in enumerate(text) if '?' == c]
        self.text = text

    def options(self, check):
        n = 0
        hashes = sum(check) - self.hashes
        for indices in combinations(self.holes, hashes):
            v = list(self.text)
            for i in indices:
                v[i] = '#'
            n += list(map(len, re.findall('#+', ''.join(v)))) == check
        return n

def main():
    def g():
        with inpath().open() as f:
            for l in f:
                u, v = l.split()
                yield Record(u).options(list(map(int, v.split(','))))
    print(sum(g()))
