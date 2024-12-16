from adventlib import inpath

def main():
    blocks = []
    for i, k in enumerate(map(int, inpath().read_text().rstrip())):
        id = None if i & 1 else i // 2
        blocks.extend(id for _ in range(k))
    i = 0
    j = len(blocks) - 1
    while True:
        while blocks[i] is not None:
            i += 1
        while blocks[j] is None:
            j -= 1
        if i >= j:
            break
        blocks[i] = blocks[j]
        blocks[j] = None
    print(sum(i * id for i, id in enumerate(blocks) if id is not None))
