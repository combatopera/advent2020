#!/usr/bin/env python3

from pathlib import Path

width = 25

class Validator:

    def __init__(self, values):
        self.ring = [0] * len(values)
        for value in values:
            self.update(value)

    def update(self, value):
        self.ring.pop(0)
        self.ring.append(value)

    def validate(self, value):
        for x in self.ring:
            for y in self.ring:
                if x != y and x + y == value:
                    return True

def main():
    with Path('input', '9').open() as f:
        v = [int(l) for l in f]
    validator = Validator(v[:width])
    print(validator.ring)
    for x in v[width:]:
        if not validator.validate(x):
            break
        validator.update(x)
    print(x)

if '__main__' == __name__:
    main()
