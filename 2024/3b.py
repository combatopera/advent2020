from adventlib import inpath
import re

def main():
    def g():
        allow = True
        for x, y, do, don_t in re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", inpath().read_text()):
            if do:
                allow = True
            elif don_t:
                allow = False
            elif allow:
                yield int(x) * int(y)
    print(sum(g()))
