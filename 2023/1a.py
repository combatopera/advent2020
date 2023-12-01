#!/usr/bin/env python3

from pathlib import Path
import re

def main():
    def g():
        for l in Path('input', '1').open():
            digits = re.findall('[0-9]', l)
            yield int(''.join(digits[i] for i in [0, -1]))
    print(sum(g()))

if '__main__' == __name__:
    main()
