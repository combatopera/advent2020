from adventlib import readchunks
from functools import reduce
from itertools import islice
from adventlib import inpath
import operator

fields = None

class Field:

    def __init__(self, name, ranges):
        self.name = name
        self.ranges = ranges

    def accept(self, value):
        return any(value in r for r in self.ranges)

def main():
    oktickets = []
    if True:
        with inpath().open() as f:
            for chunk in readchunks(f):
                if 'your ticket:' == chunk[0]:
                    myticket = [int(w) for w in chunk[1].split(',')]
                elif 'nearby tickets:' == chunk[0]:
                    for t in islice(chunk, 1, None):
                        vals = [int(w) for w in t.split(',')]
                        if all(any(f.accept(v) for f in fields) for v in vals):
                            oktickets.append(vals)
                else:
                    fields = []
                    for rule in chunk:
                        name, ranges = rule.split(': ')
                        ranges = ranges.split(' or ')
                        fields.append(Field(name, [range(min, max+1) for r in ranges for min, max in [map(int, r.split('-'))]]))
    indexsets = {f: set(range(len(fields))) for f in fields}
    indexes = {}
    while len(indexes) < len(fields):
        for t in oktickets:
            for index in range(len(fields)):
                for f, s in indexsets.items():
                    if not f.accept(t[index]):
                        s.discard(index)
        for f, s in indexsets.items():
            if 1 == len(s):
                i, = s
                indexes[f] = i
        for f in indexes:
            indexsets.pop(f, None)
        for s in indexsets.values():
            s.difference_update(indexes.values())
    print(reduce(operator.mul, (myticket[indexes[f]] for f in fields if f.name.startswith('departure'))))
