#!/usr/bin/env python3

from adventlib import answerof, SeatReader
from pathlib import Path

def main():
    s = answerof('5a')
    with Path('input', '5').open() as f:
        taken = set(SeatReader(10).read(f))
    while s in taken:
        s -= 1
    print(s)

if '__main__' == __name__:
    main()
