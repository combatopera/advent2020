from adventlib import inpath
from adventlib.intcode import Computer

def main():
    program = [int(s) for s in inpath().read_text().split(',')]
    for noun in range(100):
        for verb in range(100):
            p = program.copy()
            p[1] = noun
            p[2] = verb
            c = Computer(p)
            c.run()
            if 19690720 == c.data[0]:
                print(100 * noun + verb)
                return
