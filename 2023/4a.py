from adventlib import inpath
import re

number = re.compile('[0-9]+')

def main():
    def g():
        with inpath().open() as f:
            for l in f:
                _, l = l.split(': ')
                l, r = l.split(' | ')
                win = set(number.findall(l))
                n = sum(1 for x in number.findall(r) if x in win)
                if n:
                    yield 1 << (n - 1)
    print(sum(g()))
