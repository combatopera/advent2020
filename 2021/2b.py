from pathlib import Path

class Pos:

    h, d, a = 0, 0, 0

    def forward(self, k):
        self.h += k
        self.d += self.a * k

    def down(self, k):
        self.a += k

    def up(self, k):
        self.a -= k

def main():
    p = Pos()
    with Path('input', '2').open() as f:
        for line in f:
            w, k = line.split()
            getattr(p, w)(int(k))
    print(p.h * p.d)
