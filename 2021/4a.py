#!/usr/bin/env python3

from adventlib import readchunks
from pathlib import Path

class Board:

    def __init__(self, lines):
        self.rows = [[int(n) for n in l.split()] for l in lines]

def main():
    with Path('input', '4').open() as f:
        i = readchunks(f)
        numbers, = ([int(n) for n in l.split(',')] for l in next(i))
        boards = [Board(lines) for lines in i]

if '__main__' == __name__:
    main()
