from adventlib import inpath
from adventlib.t20 import SeatReader

def main():
    with inpath().open() as f:
        print(max(SeatReader(10).read(f)))
