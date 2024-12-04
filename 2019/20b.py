from adventlib import readgrid
from diapyr.util import bfs
from itertools import accumulate
from networkx.exception import NetworkXNoPath
from string import ascii_uppercase
import networkx as nx

moves = [(x, y) for r in [range(-1, 2)] for x in r for y in r if abs(x) ^ abs(y)]

def _markintersections(grid):
    for p, c in grid.items():
        if '.' == c and any(n > 2 for n in accumulate(1 for m in moves if p + m in grid)):
            name = ','.join(map(str, p)), 0
            grid[p] = name
            yield name

def _cullintersections(G):
    while True:
        for n in G:
            if ',' in n[0]:
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

def _graph():
    acceptchars = {'.', *ascii_uppercase}
    grid = {p: c for p, c in readgrid() if c in acceptchars}
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
                grid[mark] = name, 1 - outer
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
    return G

def main():
    template = _graph()
    G = template.copy()
    for n in template:
        if ',' not in n[0] and n[0] not in {'AA', 'ZZ'} and not n[1]:
            G.remove_node(n)
    size = 1
    while True:
        try:
            print(nx.shortest_path_length(G, ('AA', 0), ('ZZ', 0), weight = 'weight'))
            break
        except NetworkXNoPath:
            pass
        for e in template.edges(data = True):
            G.add_edge((e[0][0], e[0][1] + size), (e[1][0], e[1][1] + size), weight = e[2]['weight'])
        size += 1
