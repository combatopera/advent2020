from adventlib import readchunks
from adventlib import inpath
from string import ascii_lowercase

def main():
    def counts():
        with inpath().open() as f:
            for group in readchunks(f):
                conjunction = set(ascii_lowercase)
                conjunction.intersection_update(*group)
                yield len(conjunction)
    print(sum(counts()))
