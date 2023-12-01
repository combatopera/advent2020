from adventlib import inpath

def main():
    positions = list(map(int, inpath().read_text().split(',')))
    def fuels():
        for target in range(min(positions), max(positions)+1):
            yield sum(abs(p-target) for p in positions)
    print(min(fuels()))
