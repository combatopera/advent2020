from adventlib import inpath
from adventlib.t20 import BagRule

def main():
    colortocontained = {}
    with inpath().open() as f:
        for r in BagRule.readmany(f):
            colortocontained[r.lhs] = r.rhs
    def contains(color):
        return sum(n * (1 + contains(c)) for c, n in colortocontained[color].items())
    print(contains('shiny gold'))
