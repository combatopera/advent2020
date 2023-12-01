from pathlib import Path

def _fuel(mass):
    f = mass // 3 - 2
    return f + _fuel(f) if f > 0 else 0

def main():
    fuel = 0
    for mass in map(int, Path('input', '1').read_text().splitlines()):
        fuel += _fuel(mass)
    print(fuel)
