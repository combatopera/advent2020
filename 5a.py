#!/usr/bin/env python3

from pathlib import Path

def main():
    def g():
        with Path('input', '5').open() as f:
            for line in f:
                row = eval(f"0b{line[:7].replace('F', '0').replace('B', '1')}")
                col = eval(f"0b{line[7:10].replace('L', '0').replace('R', '1')}")
                yield row * 8 + col
    print(max(g()))

if '__main__' == __name__:
    main()
