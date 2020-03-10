import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import logging

logger = logging.getLogger('REAL-Q-VOTER-LOGGER')


def add_random_opinions(g: nx.Graph):
    """
    Initialize nodes of a graph with randomly generated opinions [-1, 1]

    :param g: nx.Graph
    """
    for i in range(len(g.nodes())):
        g.nodes[i]['opinion'] = np.random.choice([-1, 1], 1)


def calculate_magnetization(g: nx.Graph):
    """
    Calculate magnetization (mean opinion value) of the nodes in graph

    :param g: nx.Graph
    :return: magnetization
    """
    has_opinion = nx.get_node_attributes(g, 'opinion')
    if not has_opinion:
        logger.error("Cannot calculate magnetization. Graph `g` has not opinion attributes.")
        return
    opinions = np.array(list(nx.get_node_attributes(g, 'opinion').values()))
    return np.mean(opinions)


def ba_graph(n, m):
    g = nx.barabasi_albert_graph(n, m)
    add_random_opinions(g)
    return g


def main():
    g = nx.read_edgelist("../../data/soc-wiki-Vote.mtx")
    # nx.draw(g)
    # plt.show()

    ba = ba_graph(1e4, 4)
    # nx.draw(ba, node_size=30, alpha=0.2)

    res = calculate_magnetization(ba)
    print(res)

    degrees = list(map(lambda x: x[1], g.degree()))
    degrees = np.histogram(degrees, bins=50)
    plt.plot(degrees[1][:-1], degrees[0])
    plt.xscale('log')
    plt.yscale('log')
    plt.show()


if __name__ == "__main__":
    main()
