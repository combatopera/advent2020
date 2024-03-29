from adventlib import inpath, readchunks
from collections import Counter
from itertools import islice

class Template:

    def __init__(self, v):
        self.v = v

    def insert(self, rules):
        for a, b in zip(self.v, islice(self.v, 1, None)):
            yield a
            yield rules[a + b]
        yield self.v[-1]

    def answer(self):
        d = Counter()
        for c in self.v:
            d[c] += 1
        return max(d.values()) - min(d.values())

def main():
    with inpath().open() as f:
        (template,), rules = readchunks(f)
    template = Template(template)
    rules = {x: y for x, _, y in (r.split() for r in rules)}
    for _ in range(10):
        template = Template(list(template.insert(rules)))
    print(template.answer())
