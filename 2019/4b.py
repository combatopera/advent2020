from adventlib import inpath

class Value(list):

    def repair(self):
        for i in range(1, len(self)):
            self[i] = max(self[i - 1], self[i])

    def incr(self):
        i = -1
        while True:
            if self[i] < 9:
                self[i] += 1
                break
            i -= 1
        while i < -1:
            i += 1
            self[i] = self[i - 1]

    def intornone(self):
        mark = 0
        n = group = self[mark]
        repeat = False
        for i in range(1, len(self)):
            x = self[i]
            if x == group:
                if i == mark + 1 and (i == len(self) -1 or self[i + 1] != group):
                    repeat = True
            else:
                mark = i
                group = x
            n = n * 10 + x
        if repeat:
            return n

def main():
    lo, hi = inpath().read_text().split('-')
    v = Value(int(c) for c in lo)
    v.repair()
    hi = int(hi)
    n = 0
    while True:
        k = v.intornone()
        if k is not None:
            if k > hi:
                break
            n += 1
        v.incr()
    print(n)
