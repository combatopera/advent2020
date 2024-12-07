from adventlib import inpath
from adventlib.intcode import Computer
import sys

'''
ABCDabcd J
???.#### f no choice
.??##### t no choice
#..#?### t
#.##?### t
##.#??## t
####???? f a and d may both be holes

J = D and not (A and B and C)

'''


program = '''NOT A J
NOT J J
AND B J
AND C J
NOT J J
AND D J
WALK
'''

def main():
    c = Computer(map(int, inpath().read_text().split(',')), list(map(ord, program)))
    for x in c:
        if x >= 0x80:
            break
        sys.stderr.write(chr(x))
    print(x)
