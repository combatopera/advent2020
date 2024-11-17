from adventlib import inpath
from adventlib.intcode import Computer
from itertools import permutations

def main():
    def signals():
        def getesignal():
            amps = [Computer(program.copy(), [phase]) for phase in setting]
            iters = [iter(a) for a in amps]
            signal = 0
            esignal = None
            while True:
                for a, i in zip(amps, iters):
                    a.inputs.append(signal)
                    try:
                        signal = next(i)
                    except StopIteration:
                        return esignal
                esignal = signal
        for setting in permutations(range(5, 10)):
            yield getesignal()
    program = [int(s) for s in inpath().read_text().split(',')]
    print(max(signals()))
