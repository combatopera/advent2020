from adventlib import enumerate2, inpath
from itertools import islice

def main():
    ruleblock, updateblock = inpath().read_text().split('\n\n')
    rules = {tuple(map(int, l.split('|'))) for l in ruleblock.splitlines()}
    def g():
        for l in updateblock.splitlines():
            u = list(map(int, l.split(',')))
            if all((y, x) not in rules for _, (x, y) in enumerate2(u)):
                continue
            for x in u:
                index = sum(1 for r in rules if r[0] in u and r[1] == x)
                if index == len(u) // 2:
                    yield x
    print(sum(g()))
