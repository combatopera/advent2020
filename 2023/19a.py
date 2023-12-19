from adventlib import inpath, readchunks
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
            return self.op is None or self.op(part.d[self.attr], self.val)

    def __init__(self, workflows):
        self.workflows = {}
        for w in workflows:
            k, rules = w[:-1].split('{')
            self.workflows[k] = [self.Rule(r) for r in rules.split(',')]

    def _accept(self, part, name, index):
        rule = self.workflows[name][index]
        if not rule.apply(part):
            return self._accept(part, name, index + 1)
        if 'A' == rule.dest:
            return True
        if 'R' != rule.dest:
            return self._accept(part, rule.dest, 0)

    def accept(self, part):
        return self._accept(part, 'in', 0)

class Part:

    def __init__(self, info):
        self.d = {}
        for entry in info[1:-1].split(','):
            k, v = entry.split('=')
            self.d[k] = int(v)

    def score(self):
        return sum(self.d.values())

def main():
    with inpath().open() as f:
        workflows, parts = readchunks(f)
    program = Program(workflows)
    def scores():
        for part in map(Part, parts):
            if program.accept(part):
                yield part.score()
    print(sum(scores()))
