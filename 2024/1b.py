from adventlib import inpath
from collections import defaultdict

def main():
    u = []
    v = defaultdict(int)
    for l in inpath().read_text().splitlines():
        x, y = map(int, l.split())
        u.append(x)
        v[y] += 1
    print(sum(x * v[x] for x in u))
