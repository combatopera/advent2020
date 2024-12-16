from adventlib import inpath

class Gap:

    def __init__(self, i, n):
        self.i = i
        self.n = n

def main():
    blocks = []
    gaps = []
    for i, k in enumerate(map(int, inpath().read_text().rstrip())):
        id = None if i & 1 else i // 2
        if id is None:
            gaps.append(Gap(len(blocks), k))
        blocks.extend(id for _ in range(k))
    j = len(blocks) - 1
    while id >= 0:
        while blocks[j] != id:
            j -= 1
        i = j
        while i - 1 >= 0 and blocks[i - 1] == id:
            i -= 1
        n = j - i + 1
        for gap in gaps:
            if gap.n >= n:
                for k in range(n):
                    blocks[gap.i + k] = id
                    blocks[i + k] = None
                gap.i += n
                gap.n -= n
                break
        id -= 1
    print(sum(i * id for i, id in enumerate(blocks) if id is not None))
