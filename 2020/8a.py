from adventlib.handheld import Computer, Program
from adventlib import inpath

def main():
    c = Computer()
    with inpath().open() as f:
        c.exec(Program.load(f))
    print(c.accumulator)
