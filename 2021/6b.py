from adventlib import inpath
from collections import Counter

def main():
    fish = Counter()
    for timer in map(int, inpath().read_text().split(',')):
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
