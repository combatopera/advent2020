from adventlib import inpath
import re

def main():
    def search(regex, line):
        return names[re.search(regex, line).group(1)]
    def lineval(line):
        return search(lregex, line) * 10 + search(rregex, line)
    names = {}
    for i, n in enumerate('one two three four five six seven eight nine'.split()):
        k = 1 + i
        names[n] = names[str(k)] = k
    lregex = f"({'|'.join(map(re.escape, names))})"
    rregex = f".*{lregex}"
    print(sum(map(lineval, inpath().open())))
