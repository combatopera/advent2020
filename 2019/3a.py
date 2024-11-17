from adventlib import inpath, Vector

directions = {k: Vector(v) for k, v in dict(L = (-1, 0), R = (1, 0), U = (0, 1), D = (0, -1)).items()}

def main():
    snakes = []
    for route in inpath().read_text().splitlines():
        points = set()
        point = Vector((0, 0))
        snakes.append(points)
        for instruction in route.split(','):
            u = directions[instruction[0]]
            for _ in range(int(instruction[1:])):
                point += u
                points.add(point)
    print(min(p.manhattan() for p in snakes[0] & snakes[1]))
