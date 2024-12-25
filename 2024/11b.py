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

    def stone(self, remaining, x):
        if not remaining:
            return 1
        n = 0
        for y in blink(x):
            n += self.stone(remaining - 1, y)
        return n

def main():
    n = 0
    memo = Memo()
    for x in map(int, inpath().read_text().split()):
        n += memo.stone(25, x)
    print(n)
