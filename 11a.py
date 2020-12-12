#!/usr/bin/env python3

from pathlib import Path

class Seats:

    kernel = [(r, c) for r in range(-1, 2) for c in range(-1, 2) if r or c]

    def __init__(self, f):
        self.seats = {}
        for r, row in enumerate(f):
            for c, s in enumerate(row.rstrip()):
                self.seats[r, c] = s

    def round(self):
        newseats = {}
        for (r, c), s in self.seats.items():
            if '.' != s:
                occupied = sum(1 for k in self.kernel if self.seats.get((r+k[0],c+k[1])) == '#')
                if 'L' == s and not occupied:
                    s = '#'
                elif '#' == s and occupied >= 4:
                    s = 'L'
            newseats[r, c] = s
        if newseats != self.seats:
            self.seats = newseats
            return True

    def occupied(self):
        return sum(1 for s in self.seats.values() if '#' == s)

def main():
    with Path('input', '11').open() as f:
        seats = Seats(f)
    while seats.round():
        pass
    print(seats.occupied())

if '__main__' == __name__:
    main()
