#!/usr/bin/env python3

from itertools import islice
from functools import reduce
from pathlib import Path
import operator

class Bus:

    def __init__(self, offset, period):
        self.remainder = -offset % period
        self.offset = offset
        self.period = period

def main():
    with Path('input', '13').open() as f:
        buses, = islice(f, 1, None)
    buses = [Bus(offset, int(period)) for offset, period in enumerate(buses.split(',')) if 'x' != period]
    allperiods = reduce(operator.mul, (b.period for b in buses))
    def terms():
        for b in buses:
            otherperiods = allperiods // b.period
            term = 0
            while term % b.period != b.remainder:
                term += otherperiods
            yield term
    timestamp = sum(terms())
    for b in buses:
        assert 0 == (timestamp + b.offset) % b.period
    print(timestamp)

if '__main__' == __name__:
    main()
