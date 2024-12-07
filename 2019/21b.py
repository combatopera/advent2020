from adventlib import inpath
from adventlib.intcode import Computer
import sys

'''
ABCDEFGHIabcd J
>>>#???#???## t

...??????#### t

..####...#### t


...##...#####


???##???#???# t
.??###???#### t
>>?####???### t

D and
OR
not A and H
not B and H
not C and H
E and I
not A and E and F
not A and E and F and G
not B and E and F and G


'''

program = '''NOT A J
NOT J J
AND B J
AND C J
NOT J J
AND D J
AND H J
NOT A T
AND D T
AND E T
OR T J
RUN
'''

def main():
    for x in Computer(map(int, inpath().read_text().split(',')), list(map(ord, program))):
        try:
            sys.stderr.write(chr(x))
        except ValueError:
            print(x)
            break
