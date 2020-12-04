#!/usr/bin/env python3

from pathlib import Path

fields = {
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
}

def _read():
    with Path('input', '4').open() as f:
        for line in f:
            yield line.rstrip()
    yield ''

def main():
    valid = 0
    p = {}
    for l in _read():
        if l:
            p.update(e.split(':') for e in l.split(' '))
        else:
            valid += fields <= p.keys()
            p = {}
    print(valid)

if '__main__' == __name__:
    main()
