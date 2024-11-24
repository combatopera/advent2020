from adventlib import bfs, inpath, Vector
from collections import defaultdict
from functools import reduce
from itertools import accumulate
from string import ascii_lowercase, ascii_uppercase
import networkx as nx, operator

moves = [(x, y) for r in [range(-1, 2)] for x in r for y in r if abs(x) ^ abs(y)]

def _markintersections(grid):
    for p, c in grid.items():
        if '.' == c and any(n > 2 for n in accumulate(1 for m in moves if p + m in grid)):
            name = ','.join(map(str, p))
            grid[p] = name
            yield name

def _cullintersections(G):
    while True:
        for n in G:
            if ',' in n:
                edges = G.edges(n, data = True)
                if len(edges) < 3:
                    break
        else:
            break
        if 1 == len(edges):
            G.remove_node(n)
        else:
            e, f = edges
            G.remove_node(n)
            G.add_edge(e[1], f[1], weight = e[2]['weight'] + f[2]['weight'])

def main():
    grid = {}
    acceptchars = {'.', *ascii_uppercase}
    for y, line in enumerate(inpath().read_text().splitlines()):
        for x, c in enumerate(line):
            p = Vector([x, y])
            if c in acceptchars:
                grid[p] = c
    letters = set(ascii_uppercase)
    teleports = {'AA', 'ZZ'}
    seeds = []
    for p, c in grid.items():
        if c in letters:
            v = [q for m in moves for q in [p + m] if '.' == grid.get(q)]
            if v:
                tile, = v
                name = ''.join(grid[x] for x in sorted([p, p + p - tile]))
                if name in teleports:
                    mark = tile
                else:
                    teleports.add(name)
                    mark = p
                grid[mark] = name
                seeds.append(mark)
    acceptnodes = {*teleports, *_markintersections(grid)}
    G = nx.Graph()
    @bfs((p, p + m) for p in seeds for m in moves)
    def proc(e):
        prev, p = e
        if p not in grid:
            return
        start = grid[prev]
        weight = 0
        while True:
            name = grid[p]
            weight += 1
            if name in acceptnodes:
                G.add_edge(start, name, weight = weight)
                for m in moves:
                    q = p + m
                    if q != prev:
                        yield p, q
                break
            v = [q for m in moves for q in [p + m] if q in grid and q != prev]
            if not v:
                break
            prev = p
            p, = v
    _cullintersections(G)
    print(nx.shortest_path_length(G, 'AA', 'ZZ', weight = 'weight'))
