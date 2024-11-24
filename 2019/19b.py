from adventlib import inpath, Vector
from adventlib.intcode import Computer

diag = -99, 99

def main():
    def check(p):
        return next(iter(Computer(program, list(p))))
    def upper(x):
        p = Vector([x, round(x * roughgradients[0])])
        while not check(p):
            p += (0, 1)
        while check(p - (0, 1)):
            p -= (0, 1)
        return p
    def lower(x):
        p = Vector([x, round(x * roughgradients[1])])
        while not check(p):
            p -= (0, 1)
        while check(p + (0, 1)):
            p += (0, 1)
        return p
    program = list(map(int, inpath().read_text().split(',')))
    p = Vector([1000, 0])
    while not check(p):
        p += (0, 1)
    q = p
    while check(q + (0, 1)):
        q += (0, 1)
    roughgradients = p[1] / p[0], q[1] / q[0]
    toolow = 10
    hibound = 100000
    assert not check(upper(toolow) + diag)
    assert check(upper(hibound) + diag)
    while toolow + 1 < hibound:
        x = (toolow + hibound + 1) // 2
        if check(upper(x) + diag):
            hibound = x
        else:
            toolow = x
        print(toolow, hibound)
    p = upper(hibound)
    p -= (99, 0)
    print(p[0] * 10000 + p[1])
