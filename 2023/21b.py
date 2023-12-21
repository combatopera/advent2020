from adventlib import inpath, Vector

dirs = (1, 0), (0, 1), (-1, 0), (0, -1)

class Farm:

    def __init__(self, lines):
        self.rocks = set()
        for y, l in enumerate(lines):
            for x, c in enumerate(l):
                if '#' == c:
                    self.rocks.add((x, y))
                elif 'S' == c:
                    self.start = Vector([x, y])
        self.size = x + 1, y + 1

    def newfront(self, oldfront, front):
        def g():
            for t in front:
                for d in dirs:
                    u = t + d
                    if not (u % self.size in self.rocks or u in oldfront):
                        yield u
        return set(g())

class Predictor:

    def __init__(self, frontlens, diffs):
        self.frontlens = frontlens
        self.period = len(diffs)
        self.diffs = diffs

    def frontlen(self, step):
        k = max(0, (step - len(self.frontlens) + self.period) // self.period)
        step -= self.period * k
        return self.frontlens[step] + k * self.diffs[step % self.period]

def main():
    farm = Farm(inpath().read_text().splitlines())
    period, = set(farm.size)
    oldfront = set()
    front = {farm.start}
    frontlens = []
    diffs = [0 for _ in range(period)]
    predictor = Predictor(frontlens, diffs)
    prediction = [None for _ in range(2 * period)]
    step = 0
    while True:
        frontlens.append(len(front))
        if step - period >= 0:
            diffs[step % period] = frontlens[step] - frontlens[step - period]
            prediction.pop(0)
            prediction.append(predictor.frontlen(step + period))
            if frontlens[-period:] == prediction[:period]:
                break
        step += 1
        oldfront, front = front, farm.newfront(oldfront, front)
    print(sum(predictor.frontlen(step) for step in range(26501365, -1, -2)))
