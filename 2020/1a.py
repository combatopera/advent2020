from adventlib import inpath

target = 2020

def main():
    v = list(map(int, inpath().read_text().splitlines()))
    v.sort()
    i, j = 0, len(v) - 1
    while i < j:
        n = v[i] + v[j]
        if n == target:
            print(v[i] * v[j])
            return
        if n < target:
            i += 1
        else:
            j -= 1
