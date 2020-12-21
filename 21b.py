#!/usr/bin/env python3

from pathlib import Path
import re

pattern = re.compile('(.+) [(]contains (.+)[)]\n')

class Food:

    def __init__(self, ingredients, someallergens):
        self.ingredients = ingredients
        self.someallergens = someallergens

def intersect(iterables):
    i = iter(iterables)
    s = set(next(i))
    try:
        while True:
            s &= set(next(i))
    except StopIteration:
        return s

def main():
    foods = []
    with Path('input', '21').open() as f:
        for l in f:
            ingredients, allergens = pattern.fullmatch(l).groups()
            foods.append(Food(ingredients.split(' '), allergens.split(', ')))
    allergens = {a: None for f in foods for a in f.someallergens}
    while None in allergens.values():
        for a, i in allergens.items():
            if i is None:
                intersection = intersect(f.ingredients for f in foods if a in f.someallergens) - set(allergens.values())
                if 1 == len(intersection):
                    allergens[a], = intersection
    print(','.join(i for a, i in sorted(allergens.items())))

if '__main__' == __name__:
    main()
