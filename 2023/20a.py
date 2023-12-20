from adventlib import inpath
from diapyr.util import innerclass
import operator

class Button:

    @innerclass
    class Module:

        def __init__(self, dest):
            self.dest = dest

        def broadcast(self, pulse):
            for name in self.dest:
                self.post(self, name, pulse)

        def connect(self, source):
            pass

    class Broadcaster(Module):

        def send(self, source, pulse):
            self.broadcast(pulse)

    class FlipFlop(Module):

        state = 0

        def send(self, source, pulse):
            if not pulse:
                self.state = state = not self.state
                self.broadcast(state)

    class Conjunction(Module):

        def __init__(self, *args):
            super().__init__(*args)
            self.state = {}

        def connect(self, source):
            self.state[source] = 0

        def send(self, source, pulse):
            self.state[source] = pulse
            self.broadcast(any(not v for v in self.state.values()))

    class Sink(Module):

        def send(self, source, pulse):
            pass

    def __init__(self):
        self.modules = {}
        self.pulses = {p: 0 for p in range(2)}
        self.q = []
        self.draining = False

    def add(self, name, m):
        self.modules[name] = m

    def connect(self):
        for s in list(self.modules.values()):
            for d in s.dest:
                try:
                    m = self.modules[d]
                except KeyError:
                    self.modules[d] = m = self.Sink([])
                m.connect(s)

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
        b.add(name, cls(r.split(', ')))
    b.connect()
    for _ in range(4):
        b.press()
        print(b.pulses)