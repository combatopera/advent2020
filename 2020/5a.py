from adventlib import inpath, SeatReader

def main():
    with inpath().open() as f:
        print(max(SeatReader(10).read(f)))
