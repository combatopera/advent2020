from adventlib import inpath
import networkx as nx

def main():
    G = nx.Graph()
    for line in inpath().read_text().splitlines():
        e, rest = line.split(': ')
        for f in rest.split():
            G.add_edge(e, f)
    for e in nx.minimum_edge_cut(G):
        G.remove_edge(*e)
    x, y = nx.connected_components(G)
    print(len(x) * len(y))
