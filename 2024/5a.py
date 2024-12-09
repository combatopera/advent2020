from adventlib import enumerate2, inpath

def main():
    ruleblock, updateblock = inpath().read_text().split('\n\n')
    rules = {tuple(map(int, l.split('|'))) for l in ruleblock.splitlines()}
    def g():
        for l in updateblock.splitlines():
            u = list(map(int, l.split(',')))
            if all((y, x) not in rules for _, (x, y) in enumerate2(u)):
                yield u[len(u) // 2]
    print(sum(g()))
