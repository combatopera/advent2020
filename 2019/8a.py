from adventlib import inpath
from collections import defaultdict
import re

w, h = 25, 6

def main():
    def layers():
        for layer in re.findall(f".{{{w * h}}}", inpath().read_text()):
            d = defaultdict(int)
            for c in layer:
                d[int(c)] += 1
            yield d
    l = min(layers(), key = lambda l: l[0])
    print(l[1] * l[2])
