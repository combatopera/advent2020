from adventlib import inpath
from adventlib.intcode import Computer

def main():
    Computer([int(s) for s in inpath().read_text().split(',')], [1]).run()
