#!/usr/bin/env python3

from adventlib import answerof
from pathlib import Path

def main():
    target = answerof('9a')
    with Path('input', '9').open() as f:
        v = [int(l) for l in f]
    i = j = 1
    while True:
        r = v[i:j + 1]
        total = sum(r)
        if total == target:
            break
        if total < target:
            j += 1
        else:
            i += 1
        assert i <= j
    print(min(r) + max(r))

if '__main__' == __name__:
    main()
