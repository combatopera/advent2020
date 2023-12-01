from adventlib import inpath
import re

def main():
    print(sum(int(digits[0]) * 10 + int(digits[-1]) for l in inpath().open() for digits in [re.findall('[1-9]', l)]))
