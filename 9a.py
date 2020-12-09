#!/usr/bin/env python3

from pathlib import Path

width = 25

def main():
    with Path('input', '9').open() as f:
        values = [int(l) for l in f]
    ring = values[:width]
    cursor = 0
    for value in values[width:]:
        if not any(x != y and x + y == value for x in ring for y in ring):
            break
        ring[cursor] = value
        cursor = (cursor + 1) % width
    print(value)

if '__main__' == __name__:
    main()
