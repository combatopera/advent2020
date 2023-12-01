from pathlib import Path

def _cost(n):
    return n*(n+1)//2

def main():
    positions = list(map(int, Path('input', '7').read_text().split(',')))
    def fuels():
        for target in range(min(positions), max(positions)+1):
            yield sum(_cost(abs(p-target)) for p in positions)
    print(min(fuels()))
