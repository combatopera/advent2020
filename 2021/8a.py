#!/usr/bin/env python3

from pathlib import Path

def main():
    n = 0
    with Path('input', '8').open() as f:
        for line in f:
            _, digits = (s.split() for s in line.split('|'))
            for d in digits:
                n += len(d) in {2, 4, 3, 7}
    print(n)

if '__main__' == __name__:
    main()
