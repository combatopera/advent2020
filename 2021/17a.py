#!/usr/bin/env python3

from pathlib import Path
import re

def main():
    x1, x2, y1, y2 = map(int, re.findall('-?[0-9]+', Path('input', '17').read_text()))
    print(locals())

if '__main__' == __name__:
    main()
