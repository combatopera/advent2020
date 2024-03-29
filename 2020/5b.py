from adventlib import answerof, inpath
from adventlib.t20 import SeatReader

def main():
    s = answerof('5a')
    with inpath().open() as f:
        taken = set(SeatReader(10).read(f))
    while s in taken:
        s -= 1
    print(s)
