from adventlib import inpath

class Pair:

    def __init__(self, pair, score):
        self.open, self.close = pair
        self.score = score

pairs = {p.open: p for p in [
    Pair('()', 3),
    Pair('[]', 57),
    Pair('{}', 1197),
    Pair('<>', 25137),
]}
byclose = {p.close: p for p in pairs.values()}

def _error(line):
    stack = []
    for c in line:
        p = pairs.get(c)
        if p is None:
            if stack.pop(-1).close != c:
                return byclose[c].score
        else:
            stack.append(p)
    return 0

def main():
    e = 0
    with inpath().open() as f:
        for line in f:
            e += _error(line.rstrip())
    print(e)
