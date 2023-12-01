from adventlib import inpath

class Turtle:

    seast = 0
    snorth = 0
    weast = 10
    wnorth = 1
    sin = 0, 1, 0, -1
    cos = 1, 0, -1, 0

    def N(self, number):
        self.wnorth += number

    def S(self, number):
        self.wnorth -= number

    def E(self, number):
        self.weast += number

    def W(self, number):
        self.weast -= number

    def L(self, degrees):
        x = (degrees // 90) % 4
        self.weast, self.wnorth = (
            self.weast * self.cos[x] - self.wnorth * self.sin[x],
            self.wnorth * self.cos[x] + self.weast * self.sin[x],
        )

    def R(self, degrees):
        self.L(-degrees)

    def F(self, number):
        self.seast += number * self.weast
        self.snorth += number * self.wnorth

    def manhattan(self):
        return abs(self.seast) + abs(self.snorth)

def main():
    t = Turtle()
    with inpath().open() as f:
        for l in f:
            getattr(t, l[0])(int(l[1:]))
    print(t.manhattan())
