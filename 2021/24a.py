#!/usr/bin/env python3

from pathlib import Path

class Rejection(Exception): pass

class Digit:

    def __init__(self, index, instructions):
        assert 'inp w' == instructions[0]
        for c in 'xy':
            for s in instructions:
                if c in s:
                    assert f"mul {c} 0" == s
                    break
        def g():
            yield 'x = y = 0'
            for w, a, b in (s.split() for s in instructions[1:]):
                if 'add' == w:
                    yield f"{a} += {b}"
                elif 'mul' == w:
                    yield f"{a} *= {b}"
                elif 'div' == w:
                    yield f"if {a} < 0: raise Exception"
                    yield f"if {b} <= 0: raise Exception"
                    yield f"{a} //= {b}"
                elif 'mod' == w:
                    yield f"if {a} < 0: raise Rejection"
                    yield f"if {b} <= 0: raise Exception"
                    yield f"{a} %= {b}"
                elif 'eql' == w:
                    yield f"{a} = {a} == {b}"
                else:
                    raise Exception
        self.code = compile('\n'.join(g()), str(index), 'exec')
        self.index = index

    def getz(self, z, w):
        g = dict(Rejection = Rejection, z = z, w = w)
        try:
            exec(self.code, g)
            return g['z']
        except Rejection:
            pass

def main():
    lines = Path('input', '24').read_text().splitlines()
    inps = [i for i, l in enumerate(lines) if l.split()[0] == 'inp']
    digits = [Digit(k, lines[i:j]) for k, (i, j) in enumerate(zip(inps, [*inps[1:], None]))]
    nextztow = {0}
    for d in reversed(digits):
        ztow = {}
        for z in range(-20000, 20000):
            for w in range(9, 0, -1):
                if d.getz(z, w) in nextztow:
                    ztow[z] = w
                    print(d.index, ztow)
                    break
        nextztow = ztow

if '__main__' == __name__:
    main()
