from adventlib import intcos, intsin, Vector
from collections import defaultdict
from heapq import heappop, heappush
from adventlib import inpath

inf = float('inf')
steps = [Vector([intcos(x), intsin(x)]) for x in range(4)]

class State:

    def __init__(self, weights, cursor):
        self.costs = {}
        self.rcosts = defaultdict(set)
        self.allcosts = []
        for p in weights:
            self._put(p, 0 if p == cursor else inf)
        self.weights = weights

    def _put(self, p, cost):
        self.costs[p] = cost
        s = self.rcosts[cost]
        if not s:
            heappush(self.allcosts, cost)
        s.add(p)

    def _remove(self, p):
        cost = self.costs.pop(p)
        self.rcosts[cost].remove(p)
        return cost

    def update(self, cursor):
        basecost = self._remove(cursor)
        for step in steps:
            p = cursor + step
            try:
                cost = self.costs[p]
            except KeyError:
                continue
            cost_ = basecost + self.weights[p]
            if cost_ < cost:
                self._remove(p)
                self._put(p, cost_)
        while True:
            for p in self.rcosts[self.allcosts[0]]:
                return p
            heappop(self.allcosts)

def main():
    weights = {}
    for y, line in enumerate(inpath().read_text().splitlines()):
        for x, c in enumerate(line):
            weights[Vector([x, y])] = int(c)
    target = Vector([x, y])
    cursor = Vector([0, 0])
    state = State(weights, cursor)
    while cursor != target:
        cursor = state.update(cursor)
    print(state.costs[target])
