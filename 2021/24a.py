#!/usr/bin/env python3

from pathlib import Path

class NeverMind(Exception): pass

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
                    yield f"if {b} == 0: raise Exception"
                    yield f"{a} = int({a} / {b})"
                elif 'mod' == w:
                    yield f"if {a} < 0: raise NeverMind"
                    yield f"if {b} <= 0: raise Exception"
                    yield f"{a} %= {b}"
                elif 'eql' == w:
                    yield f"{a} = {a} == {b}"
                else:
                    raise Exception
        self.code = compile('\n'.join(g()), str(index), 'exec')
        self.index = index

    def getz(self, z, w):
        g = dict(NeverMind = NeverMind, z = z, w = w)
        try:
            exec(self.code, g)
            return g['z']
        except NeverMind:
            pass

def main():
    lines = Path('input', '24').read_text().splitlines()
    inps = [i for i, l in enumerate(lines) if l.split()[0] == 'inp']
    digits = [Digit(k, lines[i:j]) for k, (i, j) in enumerate(zip(inps, [*inps[1:], None]))]
    accepts = {len(inps): {0: None}}
    for d in reversed(digits):
        accept = accepts[d.index + 1]
        accepts[d.index] = {}
        for z in range(-10000, 10000):
            for w in range(1, 10):
                z_ = d.getz(z, w)
                if z_ in accept:
                    accepts[d.index][z] = w
        print(d.index, accepts[d.index])

if '__main__' == __name__:
    main()
