from adventlib import inpath

class Chunk:

    def __init__(self, i, n):
        self.i = i
        self.n = n

def main():
    files = []
    gaps = []
    block = 0
    for i, k in enumerate(map(int, inpath().read_text().rstrip())):
        (gaps if i & 1 else files).append(Chunk(block, k))
        block += k
    for id in range(len(files))[::-1]:
        file = files[id]
        for gap in gaps:
            if gap.i >= file.i:
                break
            if file.n <= gap.n:
                file.i = gap.i
                gap.i += file.n
                gap.n -= file.n
                break
    print(sum(i * id for id, f in enumerate(files) for i in range(f.i, f.i + f.n)))
