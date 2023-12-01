from adventlib import differentiate, inpath

def main():
    with inpath().open() as f:
        joltages = [int(l) for l in f]
    joltages.append(max(joltages) + 3)
    joltages.append(0)
    joltages.sort()
    diffs = differentiate(joltages)
    print(diffs.count(1) * diffs.count(3))
