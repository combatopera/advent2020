from adventlib import intcos, intsin, readgrid, Vector

class Grid(dict):

    kernel = [Vector([intcos(k), intsin(k)]) for k in range(4)]

    def _islow(self, k):
        for d in self.kernel:
            n = self.get(k + d)
            if n is not None and n <= self[k]:
                return
        return True

    def lowpoints(self):
        for k, n in self.items():
            if self._islow(k):
                yield n

def main():
    print(sum(1 + n for n in Grid(readgrid(type = int)).lowpoints()))
