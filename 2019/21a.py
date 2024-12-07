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
    for x in Computer(map(int, inpath().read_text().split(',')), list(map(ord, program))):
        try:
            sys.stderr.write(chr(x))
        except ValueError:
            print(x)
            break
