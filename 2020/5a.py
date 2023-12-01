from adventlib import SeatReader
from adventlib import inpath

def main():
    with inpath().open() as f:
        print(max(SeatReader(10).read(f)))
