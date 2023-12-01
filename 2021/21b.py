from collections import Counter, namedtuple
from adventlib import inpath

winscore = 21
die = Counter()
for a in range(1, 4):
    for b in range(1, 4):
        for c in range(1, 4):
            die[a+b+c] += 1

class Game(namedtuple('BaseGame', 'p1 s1 p2 s2')):

    def play(self, player):
        for move, n in die.items():
            g = list(self)
            g[player * 2] = pos = (self[player * 2] + move - 1) % 10 + 1
            g[player * 2 + 1] += pos
            yield type(self)(*g), n

    def score(self, player):
        return self[player * 2 + 1]

def main():
    p1, p2 = (int(l.split(':')[-1]) for l in inpath().read_text().splitlines())
    games = Counter({Game(p1, 0, p2, 0): 1})
    wins = [0, 0]
    while games:
        for player in range(2):
            items = list(games.items())
            games.clear()
            for og, m in items:
                for g, n in og.play(player):
                    n *= m
                    if g.score(player) >= winscore:
                        wins[player] += n
                    else:
                        games[g] += n
    print(max(wins))
