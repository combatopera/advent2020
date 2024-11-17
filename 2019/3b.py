from adventlib import inpath, Vector
from functools import reduce
import operator

directions = {k: Vector(v) for k, v in dict(L = (-1, 0), R = (1, 0), U = (0, 1), D = (0, -1)).items()}

def main():
    snakes = []
    for route in inpath().read_text().splitlines():
        points = {}
        point = Vector((0, 0))
        n = 0
        for instruction in route.split(','):
            u = directions[instruction[0]]
            for _ in range(int(instruction[1:])):
                point += u
                n += 1
                if point not in points:
                    points[point] = n
        snakes.append(points)
    intersections = reduce(operator.and_, (s.keys() for s in snakes))
    print(min(sum(points[p] for points in snakes) for p in intersections))
