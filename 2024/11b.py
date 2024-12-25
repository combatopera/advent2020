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

class Total:

    n = 0

    def stone(self, remaining, x):
        if not remaining:
            self.n += 1
        else:
            for y in blink(x):
                self.stone(remaining - 1, y)

def main():
    total = Total()
    for x in map(int, inpath().read_text().split()):
        total.stone(25, x)
    print(total.n)
