from adventlib import inpath
from adventlib.intcode import Computer
import sys

program = '''NOT A J
NOT J J
AND B J
AND C J
NOT J J
AND D J
AND H J
NOT A T
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
