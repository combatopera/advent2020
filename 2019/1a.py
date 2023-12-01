from adventlib import inpath

def main():
    fuel = 0
    for mass in map(int, inpath().read_text().splitlines()):
        fuel += mass // 3 - 2
    print(fuel)
