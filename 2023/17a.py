from adventlib import inpath, intcos, intsin, Vector
from collections import namedtuple
from heapq import heappop, heappush

eswn = [Vector([intcos(k), intsin(k)]) for k in range(4)]
inf = float('inf')
Task = namedtuple('Task', 's p d')

class City:

    def __init__(self, rows):
        self.blocks = {}
        for y, r in enumerate(rows):
            for x, c in enumerate(r):
                self.blocks[x, y] = int(c)
        self.target = x, y

    def _paths(self, s, p, d):
        if s < 3:
            q = p + eswn[d]
            if q in self.blocks:
                yield Task(s + 1, q, d)
        l = (d - 1) % 4
        q = p + eswn[l]
        if q in self.blocks:
            yield Task(1, q, l)
        r = (d + 1) % 4
        q = p + eswn[r]
        if q in self.blocks:
            yield Task(1, q, r)

    def _g(self, history, cost, task):
        for t in self._paths(*task):
            newcost = cost + self.blocks[t.p]
            if newcost < history.get(t, inf):
                history[t] = newcost
                if self.target != t.p:
                    yield newcost, t

    def walk(self):
        history = {}
        tasks = [[0, Task(0, Vector([0, 0]), 0)]]
        while tasks:
            for t in self._g(history, *heappop(tasks)):
                heappush(tasks, t)
        for t, cost in history.items():
            if self.target == t.p:
                yield cost

def main():
    print(min(City(inpath().read_text().splitlines()).walk()))
