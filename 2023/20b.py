from adventlib import inpath
from diapyr.util import innerclass
import operator

class Button:

    @innerclass
    class Module:

        def __init__(self, name, dest):
            self.name = name
            self.dest = dest

        def broadcast(self, pulse):
            for name in self.dest:
                self.post(self.name, name, pulse)

    class Broadcaster(Module):

        def conn(self, source):
            pass

        def send(self, source, pulse):
            self.broadcast(pulse)

    class FlipFlop(Module):

        state = 0

        def conn(self, source):
            pass

        def send(self, source, pulse):
            if not pulse:
                self.state = state = not self.state
                self.broadcast(state)

    class Conjunction(Module):

        def __init__(self, *args):
            super().__init__(*args)
            self.state = {}

        def conn(self, source):
            self.state[source] = 0

        def send(self, source, pulse):
            self.state[source] = pulse
            self.broadcast(any(not v for v in self.state.values()))

    class Sink(Module):

        state = 0

        def conn(self, source):
            pass

        def send(self, source, pulse):
            if not pulse:
                self.state = 1

    def __init__(self):
        self.modules = {}
        self.pulses = {p: 0 for p in range(2)}
        self.q = []
        self.draining = False

    def add(self, name, m):
        self.modules[name] = m

    def connect(self):
        for n, s in list(self.modules.items()):
            for d in s.dest:
                try:
                    m = self.modules[d]
                except KeyError:
                    self.modules[d] = m = self.Sink(d, [])
                m.conn(n)

    def _drain(self):
        if self.draining:
            return
        self.draining = True
        try:
            while self.q:
                source, name, pulse = self.q.pop(0)
                self.modules[name].send(source, pulse)
        finally:
            self.draining = False

    def post(self, source, name, pulse):
        self.pulses[pulse] += 1
        self.q.append([source, name, pulse])
        self._drain()

    def press(self):
        self.post(None, 'broadcaster', 0)

def main():
    b = Button()
    lookup = {'%': b.FlipFlop, '&': b.Conjunction}
    for line in inpath().read_text().splitlines():
        l, r = line.split(' -> ')
        if 'broadcaster' == l:
            cls = b.Broadcaster
            name = l
        else:
            cls = lookup[l[0]]
            name = l[1:]
        b.add(name, cls(name, r.split(', ')))
    b.connect()
    n = 0
    while not b.modules['rx'].state:
        b.press()
        n += 1
    print(n)
