from adventlib import inpath

def algo(s):
    n = 0
    for c in s:
        n = (n + ord(c)) * 17 % 256
    return n

def main():
    print(sum(map(algo, inpath().read_text().rstrip().split(','))))
