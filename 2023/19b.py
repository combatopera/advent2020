from adventlib import inpath, readchunks
from functools import reduce
import operator, re

ops = {'<': operator.lt, '>': operator.gt}

class Program:

    class Rule:

        def __init__(self, text):
            try:
                pred, self.dest = text.split(':')
            except ValueError:
                self.dest = text
                self.op = None
            else:
                m = re.search(f"[{''.join(map(re.escape, ops))}]", pred)
                self.op = ops[m.group()]
                self.attr = pred[:m.start()]
                self.val = int(pred[m.start() + 1:])

        def apply(self, part):
            if self.op is None:
                yield part, True
                return
            r = part.d[self.attr]
            first = self.op(r.start, self.val)
            last = self.op(r.stop - 1, self.val)
            if first and last:
                yield part, True
            if first:
                assert operator.lt is self.op
                yield part.replace(self.attr, range(r.start, self.val)), True
                yield part.replace(self.attr, range(self.val, r.stop)), False
            if last:
                assert operator.gt is self.op
                yield part.replace(self.attr, range(r.start, self.val + 1)), False
                yield part.replace(self.attr, range(self.val + 1, r.stop)), True

    def __init__(self, workflows):
        self.workflows = {}
        for w in workflows:
            k, rules = w[:-1].split('{')
            self.workflows[k] = [self.Rule(r) for r in rules.split(',')]

    def _accept(self, part, name, index):
        rule = self.workflows[name][index]
        for q, a in rule.apply(part):
            if not a:
                yield from self._accept(q, name, index + 1)
            elif 'A' == rule.dest:
                yield q
            elif 'R' != rule.dest:
                yield from self._accept(q, rule.dest, 0)

    def accept(self, part):
        yield from self._accept(part, 'in', 0)

class Part:

    @classmethod
    def _of(cls, *args, **kwargs):
        return cls(*args, **kwargs)

    def __init__(self, d):
        self.d = d

    def replace(self, k, v):
        return self._of({**self.d, k: v})

    def count(self):
        return reduce(operator.mul, map(len, self.d.values()))

def main():
    with inpath().open() as f:
        workflows, _ = readchunks(f)
    print(sum(part.count() for part in Program(workflows).accept(Part({k: range(1, 4001) for k in 'xmas'}))))
