from adventlib import inpath

class Turtle:

    east = 0
    north = 0
    facing = 0
    facings = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def N(self, number):
        self.north += number

    def S(self, number):
        self.north -= number

    def E(self, number):
        self.east += number

    def W(self, number):
        self.east -= number

    def L(self, degrees):
        self.facing = (self.facing + degrees // 90) % len(self.facings)

    def R(self, degrees):
        self.L(-degrees)

    def F(self, number):
        facing = self.facings[self.facing]
        self.E(number * facing[0])
        self.N(number * facing[1])

    def manhattan(self):
        return abs(self.east) + abs(self.north)

def main():
    t = Turtle()
    with inpath().open() as f:
        for l in f:
            getattr(t, l[0])(int(l[1:]))
    print(t.manhattan())
