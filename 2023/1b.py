from adventlib import inpath
import re

names = {n: 1 + i for i, n in enumerate('one two three four five six seven eight nine'.split())}
regexfirst = '([0-9]|' + '|'.join(map(re.escape, names)) + ')'
regexlast = '.*' + regexfirst
for i in range(10):
    names[str(i)] = i

def main():
    def g():
        for l in inpath().open():
            yield names[re.search(regexfirst, l).group(1)] * 10 + names[re.search(regexlast, l).group(1)]
    print(sum(g()))
