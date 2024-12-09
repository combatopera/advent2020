from adventlib import enumerate2, readgrid
from collections import defaultdict

def main():
    def offer(an):
        if all(x >= 0 and x <= m for x, m in zip(an, maxp)):
            antinodes.add(an)
            return True
    antennas = defaultdict(list)
    for p, c in readgrid():
        if '.' != c:
            antennas[c].append(p)
    maxp = p
    antinodes = set()
    for a, v in antennas.items():
        for _, (p, q) in enumerate2(v):
            u = q - p
            k = 0
            while offer(p - u * k):
                k += 1
            k = 0
            while offer(q + u * k):
                k += 1
    print(len(antinodes))
