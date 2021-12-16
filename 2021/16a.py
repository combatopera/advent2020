#!/usr/bin/env python3

from pathlib import Path

def main():
    text = Path('input', '16').read_text().rstrip()
    bits = [(i >> b) & 1 for c in text for i in [int(c, 16)] for b in range(3, -1, -1)]
    print(bits)

if '__main__' == __name__:
    main()
