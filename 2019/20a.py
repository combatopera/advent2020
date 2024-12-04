from adventlib import readgrid
from diapyr.util import bfs
from itertools import accumulate
from string import ascii_uppercase
import networkx as nx

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
    for p, c in readgrid():
        if c in acceptchars:
            grid[p] = c
    dots = [p for p, c in grid.items() if '.' == c]
    minx = min(p[0] for p in dots)
    maxx = max(p[0] for p in dots)
    miny = min(p[1] for p in dots)
    maxy = max(p[1] for p in dots)
    letters = set(ascii_uppercase)
    seeds = []
    for p, c in grid.items():
        if c in letters:
            v = [q for m in moves for q in [p + m] if '.' == grid.get(q)]
            if v:
                tile, = v
                name = ''.join(grid[x] for x in sorted([p, p + p - tile]))
                outer = tile[0] in {minx, maxx} or tile[1] in {miny, maxy}
                mark = tile if outer else p
                grid[mark] = name
                seeds.append(mark)
    acceptnodes = {*(grid[p] for p in seeds), *_markintersections(grid)}
    G = nx.Graph()
    @bfs((p, p + m) for p in seeds for m in moves)
    def proc(bfsinfo, e):
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
