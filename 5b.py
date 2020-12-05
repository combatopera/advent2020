#!/usr/bin/env python3

from adventlib import answerof, SeatReader
from pathlib import Path
import subprocess

def main():
    s = answerof('5a')
    with Path('input', '5').open() as f:
        taken = set(SeatReader(10).read(f))
    try:
        while True:
            taken.remove(s)
            s -= 1
    except KeyError:
        print(s)

if '__main__' == __name__:
    main()
