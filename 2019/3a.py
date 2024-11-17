from adventlib import inpath, Vector
from functools import reduce
import operator

directions = {k: Vector(v) for k, v in dict(L = (-1, 0), R = (1, 0), U = (0, 1), D = (0, -1)).items()}

def main():
    snakes = []
    for route in inpath().read_text().splitlines():
        points = set()
        point = Vector((0, 0))
        for instruction in route.split(','):
            u = directions[instruction[0]]
            for _ in range(int(instruction[1:])):
                point += u
                points.add(point)
        snakes.append(points)
    print(min(p.manhattan() for p in reduce(operator.and_, snakes)))
