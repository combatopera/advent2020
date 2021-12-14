#!/usr/bin/env python3

from collections import Counter
from pathlib import Path

def main():
    fish = Counter()
    for timer in map(int, Path('input', '6').read_text().split(',')):
        fish[timer] += 1
    for _ in range(256):
        fish_ = Counter()
        for timer, n in fish.items():
            if timer:
                fish_[timer - 1] += n
            else:
                fish_[6] += n
                fish_[8] += n
        fish = fish_
    print(sum(fish.values()))

if '__main__' == __name__:
    main()
