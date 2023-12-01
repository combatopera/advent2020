from adventlib import inpath, readchunks

fields = {
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
}

def main():
    valid = 0
    with inpath().open() as f:
        for chunk in readchunks(f):
            p = {}
            for l in chunk:
                p.update(e.split(':') for e in l.split(' '))
            valid += fields <= p.keys()
    print(valid)
