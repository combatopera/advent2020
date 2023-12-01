from adventlib import inpath
from adventlib.handheld import Computer, Program

def main():
    c = Computer()
    with inpath().open() as f:
        c.exec(Program.load(f))
    print(c.accumulator)
