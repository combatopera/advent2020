from adventlib import inpath

class Pos:

    h, d = 0, 0

    def forward(self, k):
        self.h += k

    def down(self, k):
        self.d += k

    def up(self, k):
        self.d -= k

def main():
    p = Pos()
    with inpath().open() as f:
        for line in f:
            w, k = line.split()
            getattr(p, w)(int(k))
    print(p.h * p.d)
