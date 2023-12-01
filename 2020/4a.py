from adventlib import readchunks
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

def main():
    valid = 0
    with Path('input', '4').open() as f:
        for chunk in readchunks(f):
            p = {}
            for l in chunk:
                p.update(e.split(':') for e in l.split(' '))
            valid += fields <= p.keys()
    print(valid)
