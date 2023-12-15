from adventlib import inpath
import re

def algo(s):
    n = 0
    for c in s:
        n = (n + ord(c)) * 17 % 256
    return n

def main():
    boxes = [{} for _ in range(256)]
    for s in inpath().read_text().rstrip().split(','):
        l, v = re.split('[=-]', s)
        box = boxes[algo(l)]
        if v:
            box[l] = v
        else:
            box.pop(l, None)
    print(sum((1 + i) * (1 + j) * int(v) for i, b in enumerate(boxes) for j, v in enumerate(b.values())))
