from adventlib import inpath

def main():
    n = 0
    with inpath().open() as f:
        for line in f:
            _, digits = (s.split() for s in line.split('|'))
            for d in digits:
                n += len(d) in {2, 4, 3, 7}
    print(n)
