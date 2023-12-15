from adventlib import inpath

def algo(s):
    n = 0
    for c in s:
        n = (n + ord(c)) * 17 % 256
    return n

def main():
    v = ''.join(inpath().read_text().splitlines()).split(',')
    print(sum(map(algo, v)))
