from adventlib import inpath

class Graph:

    def __init__(self, edges):
        self.smallnodes = {n for e in edges for n in e if n == n.lower()}
        self.edges = edges

    def _paths(self, p, visited, visited2):
        if p[-1] == 'end':
            yield p
        else:
            for e in self.edges:
                n = e - {p[-1]}
                if 1 == len(n):
                    n, = n
                    if not (n in self.smallnodes and n in visited):
                        yield from self._paths(p + [n], visited | {n}, visited2)
                    elif not (visited2 or 'start' == n):
                        yield from self._paths(p + [n], visited, {n})

    def paths(self):
        yield from self._paths(['start'], {'start'}, set())

def main():
    g = Graph([set(line.split('-')) for line in inpath().read_text().splitlines()])
    print(sum(1 for _ in g.paths()))
