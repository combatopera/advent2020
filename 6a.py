#!/usr/bin/env python3

from adventlib import readchunks
from pathlib import Path

def main():
    n = 0
    with Path('input', '6').open() as f:
        for group in readchunks(f):
            union = set()
            union.update(*group)
            n += len(union)
    print(n)

if '__main__' == __name__:
    main()
