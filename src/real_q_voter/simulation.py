import networkx as nx
import numpy as np


def add_random_opinions(g: nx.Graph):
    """
    Initialize nodes of a graph with randomly generated opinions [-1, 1]

    :param g: nx.Graph
    """
    for node in g.nodes():
        g.nodes[node]['opinion'] = np.random.choice([-1, 1], 1)


def ba_graph(n, m):
    g = nx.barabasi_albert_graph(n, m)
    add_random_opinions(g)
    return g
