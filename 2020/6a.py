from adventlib import readchunks
from itertools import chain
from adventlib import inpath

def main():
    def counts():
        with inpath().open() as f:
            for group in readchunks(f):
                yield len(set(chain(*group)))
    print(sum(counts()))
