from pathlib import Path

def main():
    fuel = 0
    for mass in map(int, Path('input', '1').read_text().splitlines()):
        fuel += mass // 3 - 2
    print(fuel)
