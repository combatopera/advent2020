from adventlib import inpath
from adventlib.intcode import Computer
from itertools import permutations

def main():
    def signals():
        for setting in permutations(range(5)):
            amps = [Computer(program.copy(), [phase]) for phase in setting]
            signal = 0
            for a in amps:
                a.inputs.append(signal)
                signal, = a
            yield signal
    program = [int(s) for s in inpath().read_text().split(',')]
    print(max(signals()))
