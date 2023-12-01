from pathlib import Path
import re

pattern = re.compile(r'(?:mask|mem\[([0-9]+)\]) = (.+)')

def main():
    memory = {}
    with Path('input', '14').open() as f:
        for l in f:
            address, rhs = pattern.fullmatch(l.rstrip()).groups()
            if address is None:
                ones = int(rhs.replace('X', '0'), 2)
                valmask = int(rhs.translate(str.maketrans('X1', '10')), 2)
            else:
                memory[int(address)] = int(rhs) & valmask | ones
    print(sum(memory.values()))
