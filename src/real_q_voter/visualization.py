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
    fig, ax = plt.subplots()

    if nx.is_directed(g):
        in_degrees, out_degrees = _extract_degrees_from_graph(g, is_directed=True)
        in_degrees = np.histogram(in_degrees, bins=bins, density=True)
        out_degrees = np.histogram(out_degrees, bins=bins, density=True)
        ax.loglog(in_degrees[1][:-1], in_degrees[0], label='in_degree')
        ax.loglog(out_degrees[1][:-1], out_degrees[0], label='out_degree')
        ax.legend()
    else:
        degrees = _extract_degrees_from_graph(g)
        degrees = np.histogram(degrees, bins=bins, density=True)
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


def plot_network(g: nx.Graph, show_opinion=False, filename=None, **plot_parameters):
    """
    Plot `g` network

    :param g: nx.Graph
    :param show_opinion: Color plot by opinion?
    :param filename: Name of the output figure
    """
    spring_layout = nx.spring_layout(g)
    opinions = None
    if show_opinion:
        opinions = np.array(list(nx.get_node_attributes(g, 'opinion').values()))
    nx.draw(g, pos=spring_layout, node_color=opinions, node_size=30,
            edge_color=[0, 0, 0, 0.2], cmap=plt.cm.jet, **plot_parameters)
    if filename:
        plt.savefig('../../figures/' + filename + '.png', bbox_inches='tight', dpi=400)
    else:
        plt.show()


def _extract_degrees_from_graph(g: nx.Graph, is_directed=False):
    if is_directed:
        in_degrees = list(map(lambda x: x[1], g.in_degree))
        out_degrees = list(map(lambda x: x[1], g.out_degree))
        return in_degrees, out_degrees
    else:
        degrees = list(map(lambda x: x[1], g.degree))
        return degrees
