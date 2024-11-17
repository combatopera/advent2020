from adventlib import inpath
from collections import defaultdict
import re

w, h = 25, 6

def main():
    layersize = w * h
    layers = []
    for layer in re.findall(f".{{{layersize}}}", inpath().read_text()):
        d = defaultdict(int)
        for c in layer:
            d[int(c)] += 1
        layers.append(d)
    l = min(layers, key = lambda l: l[0])
    print(l[1] * l[2])
