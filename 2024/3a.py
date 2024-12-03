from adventlib import inpath
from functools import reduce
import operator, re

def main():
    print(sum(reduce(operator.mul, map(int, t)) for t in re.findall(r'mul\((\d+),(\d+)\)', inpath().read_text())))
