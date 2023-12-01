from adventlib import inpath
from itertools import combinations
import re

pattern = re.compile(r'(?:mask|mem\[([0-9]+)\]) = (.+)')

def main():
    memory = {}
    with inpath().open() as f:
        for l in f:
            addrstr, rhs = pattern.fullmatch(l.rstrip()).groups()
            if addrstr is None:
                ones = int(rhs.translate(str.maketrans('X', '0')), 2)
                addrmask = int(rhs.translate(str.maketrans('X10', '001')), 2)
                floats = [2 ** i for i, c in enumerate(reversed(rhs)) if 'X' == c]
            else:
                addr0 = int(addrstr) & addrmask | ones
                val = int(rhs)
                # Adapt powerset recipe:
                for size in range(len(floats) + 1):
                    for n in map(sum, combinations(floats, size)):
                        memory[addr0 | n] = val
    print(sum(memory.values()))
