from adventlib import BagRule
from pathlib import Path

def main():
    colortocontained = {}
    with Path('input', '7').open() as f:
        for r in BagRule.readmany(f):
            colortocontained[r.lhs] = r.rhs
    def contains(color):
        return sum(n * (1 + contains(c)) for c, n in colortocontained[color].items())
    print(contains('shiny gold'))
