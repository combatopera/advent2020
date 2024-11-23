from adventlib import bfs, inpath, Vector
from string import ascii_lowercase, ascii_uppercase
import networkx as nx

acceptdoors = set(ascii_uppercase)
acceptrealnodes = {'@', *ascii_lowercase}
doormasks = {c: 1 << (ord(c) - ord('A')) for c in ascii_uppercase}
keymasks = {c: 1 << (ord(c) - ord('a')) for c in ascii_lowercase}
moves = [(x, y) for r in [range(-1, 2)] for x in r for y in r if abs(x) ^ abs(y)]

def _mainimpl(block):
    grid = {}
    for y, line in enumerate(block.splitlines()):
        for x, c in enumerate(line):
            p = Vector([x, y])
            if '#' != c:
                grid[p] = c
                if '@' == c:
                    origin = p
    def intersections():
        for p, c in grid.items():
            if '.' == c and sum(1 for m in moves if p + m in grid) > 2:
                name = ','.join(map(str, p))
                grid[p] = name
                yield name
    intersections = set(intersections())
    G = nx.Graph()
    @bfs((origin, origin + m) for m in moves)
    def proc(e):
        prev, p = e
        if p not in grid:
            return
        start = grid[prev]
        requires = 0
        weight = 0
        while True:
            name = grid[p]
            requires |= doormasks.get(name, 0)
            weight += 1
            if name in acceptrealnodes or name in intersections:
                G.add_edge(start, name, requires = requires, weight = weight)
                for m in moves:
                    q = p + m
                    if q != prev:
                        yield p, q
                break
            v = [q for m in moves for q in [p + m] if q in grid and q != prev]
            if not v:
                break
            prev = p
            p = v[0]
    maxkeys = (1 << (len(G) - 1 - len(intersections))) - 1
    H = nx.DiGraph()
    sinks = []
    @bfs([('@', 0)])
    def diproc(n):
        c, keys = n
        for e in G.edges(c, True):
            if keys | e[2]['requires'] == keys:
                dest = e[1], keys | keymasks.get(e[1], 0)
                H.add_edge(n, dest, weight = e[2]['weight'])
                if dest[1] != maxkeys:
                    yield dest
                else:
                    sinks.append(dest)
    print(min(nx.shortest_path_length(H, ('@', 0), sink, weight = 'weight') for sink in sinks))

def main():
    for block in inpath().read_text().split('\n\n'):
        _mainimpl(block)
