#!/usr/bin/env python3

from pathlib import Path

def main():
    def rating(common):
        lines = alllines
        for i in range(len(lines[0])):
            threshold = sum(ord(c) for c in '01') * len(lines) / 2
            s = sum(ord(l[i]) for l in lines)
            if s > threshold:
                keep = int(common)
            elif s < threshold:
                keep = 1 - common
            else:
                keep = int(common)
            keep = str(keep)
            lines = [l for l in lines if l[i] == keep]
            if 1 == len(lines):
                return int(lines[0], 2)
    alllines = Path('input', '3').read_text().splitlines()
    print(rating(True) * rating(False))

if '__main__' == __name__:
    main()
