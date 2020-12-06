#!/usr/bin/env python3

from adventlib import readchunks
from pathlib import Path
from string import ascii_lowercase

def main():
    def counts():
        with Path('input', '6').open() as f:
            for group in readchunks(f):
                conjunction = set(ascii_lowercase)
                conjunction.intersection_update(*group)
                yield len(conjunction)
    print(sum(counts()))

if '__main__' == __name__:
    main()
