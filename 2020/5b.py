from adventlib import answerof, SeatReader
from adventlib import inpath

def main():
    s = answerof('5a')
    with inpath().open() as f:
        taken = set(SeatReader(10).read(f))
    while s in taken:
        s -= 1
    print(s)
