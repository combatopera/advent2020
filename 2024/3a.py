from adventlib import inpath
import operator, re

def main():
    print(sum(operator.mul(*map(int, t)) for t in re.findall(r'mul\((\d+),(\d+)\)', inpath().read_text())))
