#!/usr/bin/env python3

input = '538914762'

class Cups:

    def __init__(self, cups):
        self.lo = min(cups)
        self.hi = max(cups)
        self.n = len(cups)
        self.cups = cups

    def __getitem__(self, i):
        return self.cups[i % self.n]

    def move(self):
        trio = [self.cups.pop(1) for _ in range(3)]
        label = self.cups[0]
        while True:
            label -= 1
            if label < self.lo:
                label = self.hi
            if label not in trio:
                break
        i = self.cups.index(label) + 1
        self.cups[i:i] = trio
        self.cups.append(self.cups.pop(0))

    def report(self):
        i = self.cups.index(1) + 1
        return self[i] * self[i + 1]

def main():
    v = list(map(int, input))
    cups = Cups(v + list(range(len(v)+1, 1000000+1)))
    for _ in range(10000000):
        cups.move()
    print(cups.report())

if '__main__' == __name__:
    main()
