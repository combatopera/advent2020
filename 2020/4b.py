from adventlib import readchunks
from pathlib import Path
import re

class Pattern:

    def __init__(self, regex):
        self.pattern = re.compile(regex)

    def __call__(self, text):
        return self.pattern.fullmatch(text)

class Int:

    intpattern = Pattern('[0-9]+')

    def __init__(self, min, max):
        self.r = range(min, max + 1)

    def __call__(self, text):
        return self.intpattern(text) and int(text) in self.r

class And:

    def __init__(self, *rules):
        self.rules = rules

    def __call__(self, text):
        return all(r(text) for r in self.rules)

class Switch:

    def __init__(self, key, value, rules):
        self.key = key
        self.value = value
        self.rules = rules

    def __call__(self, text):
        k = self.key(text)
        if k in self.rules:
            return self.rules[k](self.value(text))

yearpattern = Pattern('[0-9]{4}')
rules = dict(
    byr = And(yearpattern, Int(1920, 2002)),
    iyr = And(yearpattern, Int(2010, 2020)),
    eyr = And(yearpattern, Int(2020, 2030)),
    hgt = Switch(lambda s: s[-2:], lambda s: s[:-2], {'cm': Int(150, 193), 'in': Int(59, 76)}),
    hcl = Pattern('#[0-9a-f]{6}'),
    ecl = lambda s: s in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
    pid = Pattern('[0-9]{9}'),
)

def main():
    valid = 0
    with Path('input', '4').open() as f:
        for chunk in readchunks(f):
            p = {}
            for l in chunk:
                p.update(e.split(':') for e in l.split(' '))
            valid += all(f in p and rule(p[f]) for f, rule in rules.items())
    print(valid)
