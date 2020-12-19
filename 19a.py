#!/usr/bin/env python3

from adventlib import readchunks
from pathlib import Path

class Ref:

    def __init__(self, rules, index):
        self.rules = rules
        self.index = index

    def __getattr__(self, name):
        return getattr(self.rules[self.index], name)

class Rule:

    def accept(self, m):
        return any(len(m) == n for n in self.consume(m, 0))

class Char(Rule):

    @classmethod
    def parse(cls, rules, text):
        try:
            return Ref(rules, int(text))
        except ValueError:
            return cls(text[1])

    def __init__(self, c):
        self.c = c

    def consume(self, m, i):
        if m[i] == self.c:
            yield 1

class Seq(Rule):

    @classmethod
    def parse(cls, rules, text):
        seq = text.split(' ')
        return Char.parse(rules, text) if 1 == len(seq) else cls([Char.parse(rules, w) for w in seq])

    @classmethod
    def _of(cls, rules):
        return cls(rules)

    def __init__(self, rules):
        self.rules = rules

    def consume(self, m, i):
        g = self.rules[0].consume(m, i)
        if 1 == len(self.rules):
            yield from g
        else:
            for n0 in g:
                for n1 in self._of(self.rules[1:]).consume(m, i + n0):
                    yield n0 + n1

class Or(Rule):

    @classmethod
    def parse(cls, rules, text):
        disjunction = text.split(' | ')
        return Seq.parse(rules, text) if 1 == len(disjunction) else cls([Seq.parse(rules, w) for w in disjunction])

    def __init__(self, rules):
        self.rules = rules

    def consume(self, m, i):
        for r in self.rules:
            yield from r.consume(m, i)

def main():
    rules = {}
    with Path('input', '19').open() as f:
        rulelines, messages = readchunks(f)
        for r in rulelines:
            i, text = r.split(': ')
            rules[int(i)] = Or.parse(rules, text)
        print(sum(1 for m in messages if rules[0].accept(m)))

if '__main__' == __name__:
    main()
