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
    for node in g.nodes():
        g.nodes[node]['opinion'] = np.random.choice([-1, 1], 1)


def _has_not_opinion(g: nx.Graph) -> bool:
    """
    Check if `g` has `opinion` attribute

    :param g: nx.Graph
    :return: True if `g` has `opinion` attribute, False otherwise
    """
    if not nx.get_node_attributes(g, 'opinion'):
        return True
    return False


def calculate_mean_opinion(g: nx.Graph):
    """
    Calculate mean opinion <s> of the nodes in graph

    :param g: nx.Graph
    :return: mean opinion: float
    """
    if _has_not_opinion(g):
        logger.error("Cannot calculate mean opinion. Graph `g` has not attribute: `opinion`")
        return
    opinions = np.array(list(nx.get_node_attributes(g, 'opinion').values()))
    return np.mean(opinions)


def calculate_weighted_mean_opinion(g: nx.Graph):
    """
    Calculate weighted mean opinion <s * k> of the nodes in graph, where `k` is node's degree

    :param g: nx.Graph
    :return: weighted mean opinion: float
    """
    if _has_not_opinion(g):
        logger.error("Cannot calculate weighted mean opinion. Graph `g` has not attribute: `opinion`")
        return
    weights = []
    opinions = []
    for node in g.nodes():
        opinion = g.nodes[node]['opinion']
        weight = g.degree[node]
        weights.append(weight)
        opinions.append(opinion)
    return np.average(np.array(opinions), weights=np.array(opinions))


def ba_graph(n, m):
    g = nx.barabasi_albert_graph(n, m)
    add_random_opinions(g)
    return g


def plot_degree_distribution(g, bins=50):
    degrees = list(map(lambda x: x[1], g.degree()))
    degrees = np.histogram(degrees, bins=bins)
    plt.plot(degrees[1][:-1], degrees[0])
    plt.xscale('log')
    plt.yscale('log')
    plt.show()


def main():
    g = nx.read_edgelist("../../data/soc-wiki-Vote.mtx")
    add_random_opinions(g)
    # nx.draw(g)
    # plt.show()

    ba = ba_graph(1e4, 4)
    # nx.draw(ba, node_size=30, alpha=0.2)

    res = calculate_weighted_mean_opinion(ba)
    print(res)

    plot_degree_distribution(g)


if __name__ == "__main__":
    main()
