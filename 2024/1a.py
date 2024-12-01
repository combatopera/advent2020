from adventlib import inpath

def main():
    u = []
    v = []
    for l in inpath().read_text().splitlines():
        x, y = map(int, l.split())
        u.append(x)
        v.append(y)
    u.sort()
    v.sort()
    print(sum(abs(x - y) for x, y in zip(u, v)))
