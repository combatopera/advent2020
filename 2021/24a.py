#!/usr/bin/env python3

from pathlib import Path

class Rejection(Exception): pass

class Digit:

    def __init__(self, name, instructions):
        assert 'inp w' == instructions[0]
        for c in 'xy':
            for s in instructions:
                if c in s:
                    assert f"mul {c} 0" == s
                    break
            else:
                raise Exception
        def g():
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
                    yield f"{a} = 1 if {a} == {b} else 0"
                else:
                    raise Exception
        text = '\n'.join(g())
        self.code = compile(text, name, 'exec')

    def getz(self, z, w):
        g = dict(Rejection = Rejection, z = z, w = w, x = 987, y = 654)
        try:
            exec(self.code, g)
            return g['z']
        except Rejection:
            pass

def main():
    lines = Path('input', '24').read_text().splitlines()
    inps = [i for i, l in enumerate(lines) if l.split()[0] == 'inp']
    digits = [Digit(str(k), lines[i:j]) for k, (i, j) in enumerate(zip(inps, [*inps[1:], None]))]
    def g():
        nextztow = {0}
        for d in reversed(digits):
            ztow = {}
            for z in range(-1000000, 1000000):
                for w in range(9, 0, -1):
                    if d.getz(z, w) in nextztow:
                        ztow[z] = w
                        break
            yield ztow
            nextztow = ztow
    digittoztow = list(g())
    digittoztow.reverse()
    def h():
        z = 0
        for d, ztow in zip(digits, digittoztow):
            w = ztow[z]
            yield w
            z = d.getz(z, w)
    print(''.join(map(str, h())))

if '__main__' == __name__:
    main()
