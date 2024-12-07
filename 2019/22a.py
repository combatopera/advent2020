from adventlib import inpath

def main():
    for l in inpath().read_text().splitlines():
        print(l)
