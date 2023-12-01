from adventlib import inpath

class Die:

    last = 100
    n = 0

    def roll(self):
        self.last = self.last % 100 + 1
        self.n += 1
        return self.last

def main():
    players = [int(l.split(':')[-1]) for l in inpath().read_text().splitlines()]
    scores = [0 for _ in players]
    d = Die()
    while True:
        for i, p in enumerate(players):
            n = sum(d.roll() for _ in range(3))
            players[i] = p = (p + n - 1) % 10 + 1
            scores[i] += p
            if scores[i] >= 1000:
                print(scores[1 - i] * d.n)
                return
