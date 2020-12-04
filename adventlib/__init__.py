def readchunks(f):
    def g():
        for l in f:
            yield l.rstrip()
        yield ''
    chunk = []
    for l in g():
        if l:
            chunk.append(l)
        elif chunk:
            yield chunk.copy()
            chunk.clear()
