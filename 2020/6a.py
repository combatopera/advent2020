from adventlib import readchunks
from itertools import chain
from pathlib import Path

def main():
    def counts():
        with Path('input', '6').open() as f:
            for group in readchunks(f):
                yield len(set(chain(*group)))
    print(sum(counts()))
