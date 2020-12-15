#!/usr/bin/env python3

from collections import defaultdict
from pathlib import Path

totalturns = 30000000

def main():
    t1 = {}
    t2 = {}
    turn = 1
    with Path('input', '15').open() as f:
        for n in map(int, f.read().split(',')):
            t1[n] = t2.get(n)
            t2[n] = turn
            turn += 1
    while turn <= totalturns:
        n = t2[n] - t1[n] if t1.get(n) else 0
        t1[n] = t2.get(n)
        t2[n] = turn
        turn += 1

        if not turn%1000000:print(turn)

    print(n)

if '__main__' == __name__:
    main()
