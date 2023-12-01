from adventlib import inpath
from itertools import islice

class Bus:

    def __init__(self, offset, period):
        self.remainder = -offset % period
        self.period = period

def main():
    with inpath().open() as f:
        buses, = islice(f, 1, None)
    buses = [Bus(offset, int(period)) for offset, period in enumerate(buses.split(',')) if 'x' != period]
    # Chinese remainder theorem, search by sieving:
    prevperiods = 1
    timestamp = 0
    for b in buses:
        while timestamp % b.period != b.remainder:
            timestamp += prevperiods
        prevperiods *= b.period
    print(timestamp)
