#!/usr/bin/env python3

from pathlib import Path

target = 2020

def main():
    v = list(map(int, Path('input', '1').read_text().splitlines()))
    v.sort()
    i, j = 0, len(v) - 1
    while i < j:
        n = v[i] + v[j]
        if n == target:
            print(v[i] * v[j])
            return
        if n < target:
            i += 1
        else:
            j -= 1

if '__main__' == __name__:
    main()
