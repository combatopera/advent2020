#!/usr/bin/env python3

from pathlib import Path

target = 2020

def main():
    v = list(map(int, Path('input', '1').read_text().splitlines()))
    v.sort()
    k = len(v) - 1
    while k >= 2:
        i, j = 0, k - 1
        while i < j:
            n = v[i] + v[j] + v[k]
            if n == target:
                print(v[i] * v[j] * v[k])
                return
            if n < target:
                i += 1
            else:
                j -= 1
        k -= 1

if '__main__' == __name__:
    main()
