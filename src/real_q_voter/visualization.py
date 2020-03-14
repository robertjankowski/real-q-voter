import matplotlib.ticker
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def plot_degree_distribution(g: nx.Graph, bins=50, filename=None):
    """
    Plot degree distribution of given `g` graph.

    :param g: nx.Graph
    :param bins: number of bins for histogram
    :param filename: Name of the output figure
    """
    degrees = list(map(lambda x: x[1], g.degree))
    degrees = np.histogram(degrees, bins=bins, density=True)
    fig, ax = plt.subplots()
    ax.loglog(degrees[1][:-1], degrees[0])
    ax.set_xlabel('k')
    ax.set_ylabel('P(k)')
    ax.tick_params(which="minor", axis="x", direction="in")
    ax.tick_params(which="minor", axis="y", direction="in")
    ax.tick_params(which="major", axis="x", direction="in")
    ax.tick_params(which="major", axis="y", direction="in")

    if filename:
        plt.savefig('../../figures/' + filename + '.png', bbox_inches='tight', dpi=400)
    else:
        plt.show()


def plot_network(g: nx.Graph, filename=None, **parameters):
    """
    Plot `g` network

    :param g: nx.Graph
    :param filename: Name of the output figure
    """
    nx.draw(g, node_size=30, alpha=0.2, **parameters)
    if filename:
        plt.savefig('../../figures/' + filename + '.png', bbox_inches='tight', dpi=400)
    else:
        plt.show()
