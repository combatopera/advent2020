from adventlib import inpath
from collections import defaultdict
import re

class Recipe:

    def __init__(self, spec, unit):
        self.spec = spec
        self.unit = unit

    def fire(self, stock, minamount):
        times = (minamount + self.unit - 1) // self.unit
        for key, amount in self.spec.items():
            stock[key] -= amount * times
        return self.unit * times

def orefor(recipes, fuel):
    stock = defaultdict(int)
    recipes['FUEL'].fire(stock, fuel)
    while True:
        subset = {k: s for k, s in stock.items() if s < 0 and 'ORE' != k}
        if not subset:
            break
        for k, s in subset.items():
            stock[k] += recipes[k].fire(stock, -s)
    return -stock['ORE']

def main():
    recipes = dict(ORE = Recipe({}, 1))
    for line in inpath().read_text().splitlines():
        *spec, (amount, key) = re.findall('([0-9]+) ([A-Z]+)', line)
        recipes[key] = Recipe({k: int(s) for s, k in spec}, int(amount))
    lobound = 1
    toohigh = 9999999
    maxore = 1000000000000
    while True:
        fuel = (lobound + toohigh) // 2
        if fuel == lobound:
            break
        ore = orefor(recipes, fuel)
        if ore > maxore:
            toohigh = fuel
        elif ore <= maxore:
            lobound = fuel
    print(fuel)
