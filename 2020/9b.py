from adventlib import answerof, inpath

def main():
    target = answerof('9a')
    with inpath().open() as f:
        v = [int(l) for l in f]
    i = j = 1
    total = v[i]
    while total != target:
        if total < target:
            j += 1
            total += v[j]
        else:
            total -= v[i]
            i += 1
        assert i <= j
    r = v[i:j + 1]
    print(min(r) + max(r))
