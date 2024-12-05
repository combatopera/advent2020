from adventlib import inpath
from itertools import islice

def enumerate2(v):
    for j, y in enumerate(v):
        for i, x in enumerate(islice(v, j)):
            yield (i, j), (x, y)

def main():
    ruleblock, updateblock = inpath().read_text().split('\n\n')
    rules = {tuple(map(int, l.split('|'))) for l in ruleblock.splitlines()}
    def g():
        for l in updateblock.splitlines():
            u = list(map(int, l.split(',')))
            if all(t in rules for _, t in enumerate2(u)):
                yield u[len(u) // 2]
    print(sum(g()))
