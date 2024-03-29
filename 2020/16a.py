from adventlib import inpath, readchunks
from itertools import islice

fields = None

def main():
    def badvals():
        with inpath().open() as f:
            for chunk in readchunks(f):
                if 'your ticket:' == chunk[0]:
                    pass
                elif 'nearby tickets:' == chunk[0]:
                    for t in islice(chunk, 1, None):
                        vals = [int(w) for w in t.split(',')]
                        for v in vals:
                            if all(v not in r for ranges in fields.values() for r in ranges):
                                yield v
                else:
                    fields = {}
                    for rule in chunk:
                        name, ranges = rule.split(': ')
                        ranges = ranges.split(' or ')
                        fields[name] = [range(min, max+1) for r in ranges for min, max in [map(int, r.split('-'))]]
    print(sum(badvals()))
