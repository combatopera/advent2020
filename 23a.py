#!/usr/bin/env python3

from itertools import chain, islice

input = '538914762'

class Cup:

    def __init__(self, label):
        self.label = label

class Cups:

    def __init__(self, labels, n):
        self.labeltocup = {l: Cup(l) for l in labels}
        for l in range(len(self.labeltocup) + 1, n + 1):
            self.labeltocup[l] = Cup(l)
        self.current = next(iter(self.labeltocup.values()))
        for c, d in zip(self.labeltocup.values(), chain(islice(self.labeltocup.values(), 1, None), [self.current])):
            c.succ = d
            d.prev = c
        self.n = n

    def _pop3(self):
        trio = self.current.succ
        self.current.succ = trio.succ.succ.succ
        self.current.succ.prev = self.current
        return trio

    def move(self):
        trio = self._pop3()
        badlabels = {trio.label, trio.succ.label, trio.succ.succ.label}
        label = self.current.label
        while True:
            label = (label - 2) % self.n + 1
            if label not in badlabels:
                break
        before = self.labeltocup[label]
        before.succ.prev = trio.succ.succ
        trio.succ.succ.succ = before.succ
        before.succ = trio
        trio.prev = before
        self.current = self.current.succ

    def report(self):
        root = self.labeltocup[1]
        def labels():
            d = root.succ
            while d != root:
                yield d.label
                d = d.succ
        return ''.join(map(str, labels()))

def main():
    cups = Cups(map(int, input), len(input))
    for _ in range(100):
        cups.move()
    print(cups.report())

if '__main__' == __name__:
    main()
