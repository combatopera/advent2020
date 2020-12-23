#!/usr/bin/env python3

input = '538914762'

class Cups:

    def __init__(self, cups):
        self.n = len(cups)
        self.cups = cups

    def __getitem__(self, i):
        return self.cups[i % self.n]

    def move(self):
        trio = [self.cups.pop(1) for _ in range(3)]
        label = self.cups[0]
        while True:
            label -= 1
            if label < 1:
                label = self.n
            if label not in trio:
                break
        i = self.cups.index(label) + 1
        self.cups[i:i] = trio
        self.cups.append(self.cups.pop(0))

    def report(self):
        i = self.cups.index(1) + 1
        return ''.join(str(self[i + k]) for k in range(self.n - 1))

def main():
    cups = Cups(list(map(int, input)))
    for _ in range(100):
        cups.move()
    print(cups.report())

if '__main__' == __name__:
    main()
