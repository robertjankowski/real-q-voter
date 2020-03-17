import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def plot_degree_distribution(g: nx.Graph, bins=50, filename=None):
    """
    Plot degree distribution of given `g` graph.

    :param g: nx.Graph (directed or undirected)
    :param bins: number of bins for histogram
    :param filename: Name of the output figure
    """
    degrees = _extract_degrees_from_graph(g)
    degrees = np.histogram(degrees, bins=bins, density=True)
    fig, ax = plt.subplots()

    if _is_directed_graph(g):
        in_degrees, out_degrees = _extract_degrees_from_graph(g, is_directed=True)
        in_degrees = np.histogram(in_degrees, bins=bins, density=True)
        out_degrees = np.histogram(out_degrees, bins=bins, density=True)
        ax.loglog(in_degrees[1][:-1], in_degrees[0], label='in_degree')
        ax.loglog(out_degrees[1][:-1], out_degrees[0], label='out_degree')
        ax.legend()
    else:
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


def _is_directed_graph(g: nx.Graph) -> bool:
    return nx.is_directed(g)


def _extract_degrees_from_graph(g: nx.Graph, is_directed=False):
    if is_directed:
        in_degrees = list(map(lambda x: x[1], g.in_degree))
        out_degrees = list(map(lambda x: x[1], g.out_degree))
        return in_degrees, out_degrees
    else:
        degrees = list(map(lambda x: x[1], g.degree))
        return degrees
