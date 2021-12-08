#!/usr/bin/env python3

from pathlib import Path

def main():
    with Path('input', '8').open() as f:
        for line in f:
            patterns, digits = (s.split() for s in line.split('|'))
            print(patterns, digits)

if '__main__' == __name__:
    main()
