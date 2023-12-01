from adventlib import readchunks, Vector
from pathlib import Path

tile = [Vector([x, y]) for y in range(-1, 2) for x in range(-1, 2)]
infinity = Vector([float('inf')] * 2)

class Image:

    border = 0

    def __init__(self, pixels):
        self.pixels = pixels

    def _number(self, p, borderpixels_add = lambda q: None):
        n = 0
        for d in tile:
            q = p + d
            if q in self.pixels:
                k = self.pixels[q]
            else:
                borderpixels_add(q)
                k = self.border
            n = (n << 1) + k
        return n

    def apply(self, algo):
        pixels = {}
        borderpixels = set()
        for p in self.pixels:
            pixels[p] = algo[self._number(p, borderpixels.add)]
        for p in borderpixels:
            pixels[p] = algo[self._number(p)]
        self.pixels = pixels
        border = algo[self._number(infinity)]
        assert border != self.border
        self.border = border

    def lit(self):
        assert not self.border
        return sum(self.pixels.values())

def main():
    with Path('input', '20').open() as f:
        (algo,), lines = readchunks(f)
    algo = ['#' == c for c in algo]
    image = Image({Vector([x, y]): '#' == c for y, l in enumerate(lines) for x, c in enumerate(l)})
    for _ in range(2):
        image.apply(algo)
    print(image.lit())
