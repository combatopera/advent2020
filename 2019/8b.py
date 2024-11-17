from adventlib import inpath
import re

w, h = 25, 6

def _coords():
    for y in range(h):
        for x in range(w):
            yield x, y

def main():
    image = {p: 2 for p in _coords()}
    for layer in re.findall(f".{{{w * h}}}", inpath().read_text()):
        for p, c in zip(_coords(), map(int, layer)):
            if image[p] == 2:
                image[p] = c
    for y in range(h):
        print(''.join('#' if image[x, y] else ' ' for x in range(w)))
