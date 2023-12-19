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
            if self.op is None or self.op(part.d[self.attr], self.val):
                return self.dest

    def __init__(self, workflows):
        self.workflows = {}
        for w in workflows:
            k, rules = w[:-1].split('{')
            self.workflows[k] = [self.Rule(r) for r in rules.split(',')]

    def accept(self, part):
        w = self.workflows['in']
        while True:
            for r in w:
                dest = r.apply(part)
                if dest is not None:
                    break
            if 'A' == dest:
                return True
            if 'R' == dest:
                break
            w = self.workflows[dest]

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
