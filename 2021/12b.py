#!/usr/bin/env python3

from pathlib import Path

class Graph:

    def __init__(self, edges):
        self.smallnodes = {n for e in edges for n in e if n == n.lower()}
        self.edges = edges

    def _paths(self, p, visited, visited2):
        if p[-1] == 'end':
            yield p
        else:
            for e in self.edges:
                if p[-1] in e:
                    n, = (n for n in e if n != p[-1])
                    if not (n in self.smallnodes and n in visited):
                        yield from self._paths(p + [n], visited | {n}, visited2)
                    elif 'start' != n and not visited2:
                        yield from self._paths(p + [n], visited, {n})

    def paths(self):
        yield from self._paths(['start'], {'start'}, set())

def main():
    g = Graph([set(line.split('-')) for line in Path('input', '12').read_text().splitlines()])
    print(sum(1 for _ in g.paths()))

if '__main__' == __name__:
    main()
