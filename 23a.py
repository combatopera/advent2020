#!/usr/bin/env python3

input = '538914762'

class Cups:

    def __init__(self, n):
        self.cups = [1 + i for i in range(n)]
        self.n = n

    def load(self, labels):
        for i, l in enumerate(labels):
            self.cups[i] = l

    def __getitem__(self, i):
        return self.cups[i % self.n]

    def move(self):
        trio = [self.cups.pop(1) for _ in range(3)]
        label = self.cups[0]
        while True:
            label = (label - 2) % self.n + 1
            if label not in trio:
                break
        i = self.cups.index(label) + 1
        self.cups[i:i] = trio
        self.cups.append(self.cups.pop(0))

    def report(self):
        i = self.cups.index(1) + 1
        return ''.join(str(self[i + k]) for k in range(self.n - 1))

def main():
    cups = Cups(len(input))
    cups.load(map(int, input))
    for _ in range(100):
        cups.move()
    print(cups.report())

if '__main__' == __name__:
    main()
