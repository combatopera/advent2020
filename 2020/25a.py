from adventlib import inpath

class Loop:

    value = 1

    def __init__(self, subject):
        self.subject = subject

    def step(self):
        self.value = self.value * self.subject % 20201227

def main():
    with inpath().open() as f:
        publickeys = [int(l) for l in f]
    loop = Loop(7)
    size = 0
    while publickeys[0] != loop.value and publickeys[1] != loop.value:
        loop.step()
        size += 1
    loop = Loop(publickeys[1] if publickeys[0] == loop.value else publickeys[0])
    for _ in range(size):
        loop.step()
    print(loop.value)
