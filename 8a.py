#!/usr/bin/env python3

from adventlib.handheld import Computer, Program
from pathlib import Path

def main():
    c = Computer()
    with Path('input', '8').open() as f:
        c.exec(Program.load(f))
    print(c.accumulator)

if '__main__' == __name__:
    main()
