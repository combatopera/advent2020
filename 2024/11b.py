from adventlib import inpath

def blink(x):
    if not x:
        yield 1
    else:
        s = str(x)
        i, r = divmod(len(s), 2)
        if not r:
            yield int(s[:i])
            yield int(s[i:])
        else:
            yield 2024 * x

class Memo:

    def __init__(self):
        self.memo = {}

    def stone(self, remaining, x):
        try:
            return self.memo[remaining, x]
        except KeyError:
            pass
        n = sum(self.stone(remaining - 1, y) for y in blink(x)) if remaining else 1
        self.memo[remaining, x] = n
        return n

def main():
    n = 0
    memo = Memo()
    for x in map(int, inpath().read_text().split()):
        n += memo.stone(25, x)
    print(n)
