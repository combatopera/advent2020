#!/usr/bin/env python3

from adventlib import SeatReader
from pathlib import Path

def main():
    with Path('input', '5').open() as f:
        print(max(SeatReader(10).read(f)))

if '__main__' == __name__:
    main()
