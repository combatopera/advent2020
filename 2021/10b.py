from pathlib import Path

class Pair:

    def __init__(self, pair, score):
        self.open, self.close = pair
        self.score = score

pairs = {p.open: p for p in [
    Pair('()', 1),
    Pair('[]', 2),
    Pair('{}', 3),
    Pair('<>', 4),
]}

def _score(line):
    stack = []
    for c in line:
        p = pairs.get(c)
        if p is None:
            if stack.pop(-1).close != c:
                return
        else:
            stack.append(p)
    score = 0
    for p in reversed(stack):
        score = score * 5 + p.score
    return score

def main():
    scores = []
    with Path('input', '10').open() as f:
        for line in f:
            s = _score(line.rstrip())
            if s is not None:
                scores.append(s)
    scores.sort()
    print(scores[len(scores) // 2])
