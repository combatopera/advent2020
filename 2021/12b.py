#!/usr/bin/env python3

from pathlib import Path

class Graph:

    def __init__(self, edges):
        self.smallnodes = {n for e in edges for n in e if n == n.lower()}
        self.edges = edges

    def _paths(self, p, restrict):
        if p[-1] == 'end':
            yield p
        else:
            for e in self.edges:
                if p[-1] in e:
                    n, = (n for n in e if n != p[-1])
                    if 'start' != n:
                        if n in restrict:
                            k = restrict[n]
                            if not k or 2 not in restrict.values():
                                yield from self._paths(p + [n], dict(restrict, **{n: k + 1}))
                        else:
                            yield from self._paths(p + [n], restrict)

    def paths(self):
        yield from self._paths(['start'], {n: 0 for n in self.smallnodes})

def main():
    g = Graph([set(line.split('-')) for line in Path('input', '12').read_text().splitlines()])
    print(sum(1 for _ in g.paths()))

if '__main__' == __name__:
    main()
