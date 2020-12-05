#!/usr/bin/env python3

from adventlib import SeatReader
from pathlib import Path

def main():
    r = SeatReader(10)
    seats = set(r.range())
    with Path('input', '5').open() as f:
        seats.difference_update(r.read(f))
    try:
        for s in r.range():
            seats.remove(s)
    except KeyError:
        print(min(seats))

if '__main__' == __name__:
    main()
