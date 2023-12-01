from adventlib import inpath, readchunks
from itertools import chain

def main():
    def counts():
        with inpath().open() as f:
            for group in readchunks(f):
                yield len(set(chain(*group)))
    print(sum(counts()))
