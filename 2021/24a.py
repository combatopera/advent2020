#!/usr/bin/env python3

from pathlib import Path

def comp(name, instructions):
    assert 'inp w' == instructions[0]
    for c in 'xy':
        for s in instructions:
            if c in s:
                assert f"mul {c} 0" == s
                break
    def g():
        yield 'x = y = 0'
        for s in instructions[1:]:
            s = s.split()
            assert 'inp' != s[0]
            if 'add' == s[0]:
                yield f"{s[1]} += {s[2]}"
            elif 'mul' == s[0]:
                yield f"{s[1]} *= {s[2]}"
            elif 'div' == s[0]:
                yield f"{s[1]} = int({s[1]} / {s[2]})"
            elif 'mod' == s[0]:
                yield f"{s[1]} %= {s[2]}"
            elif 'eql' == s[0]:
                yield f"{s[1]} = int({s[1]} == {s[2]})"
            else:
                raise Exception
    text = ''.join(f"{l}\n" for l in g())
    print(text)
    return compile(text, name, 'exec')

def main():
    lines = Path('input', '24').read_text().splitlines()
    inps = [i for i, l in enumerate(lines) if l.split()[0] == 'inp']
    digits = [comp(str(k), lines[i:j]) for i, j, k in zip(inps, inps[1:]+[None], range(len(inps)))]
    for d in digits:
        for w in range(1, 10):
            for z in range(-1000, 1000):
                g = dict(w = w, z = z)
                exec(d, g)
                if not g['z']:
                    print(d, w, z)

if '__main__' == __name__:
    main()
