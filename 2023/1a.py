from adventlib import inpath
import re

def main():
    def g():
        for l in inpath().open():
            digits = re.findall('[0-9]', l)
            yield int(''.join(digits[i] for i in [0, -1]))
    print(sum(g()))
