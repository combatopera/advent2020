#!/usr/bin/env python3

from pathlib import Path

def _fuel(mass):
    f = mass // 3 - 2
    if f <= 0:
        return 0
    return f + _fuel(f)

def main():
    fuel = 0
    for mass in map(int, Path('input', '1').read_text().splitlines()):
        fuel += _fuel(mass)
    print(fuel)

if '__main__' == __name__:
    main()
