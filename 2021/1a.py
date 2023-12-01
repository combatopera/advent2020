from itertools import islice
from pathlib import Path

def main():
    print(sum(1 for v in [list(map(int, Path('input', '1').read_text().splitlines()))] for x, y in zip(v, islice(v, 1, None)) if x < y))
