#!/usr/bin/env python3

from collections import defaultdict
from pathlib import Path

def main():
    def speak(n):
        turns[n] = [*turns[n][-1:], turn]
    turns = defaultdict(list)
    turn = 0
    with Path('input', '15').open() as f:
        for n in map(int, f.read().split(',')):
            turn += 1
            speak(n)
    while turn != 2020:
        turn += 1
        if len(turns[n]) < 2:
            n = 0
        else:
            n = turns[n][1] - turns[n][0]
        speak(n)
    print(n)

if '__main__' == __name__:
    main()
