import networkx as nx
import numpy as np

from src.real_q_voter.logger import get_logger

logger = get_logger('REAL-Q-VOTER-OPINION-LOGGER')


def add_random_opinions(g: nx.Graph):
    """
    Initialize nodes of a graph with randomly generated opinions [-1, 1]

    :param g: nx.Graph
    """
    for node in g.nodes():
        g.nodes[node]['opinion'] = np.random.choice([-1, 1], 1)


def add_positive_opinions(g: nx.Graph):
    """
    Add positive opinion (+1) to every agent

    :param g: nx.Graph
    """
    _add_single_opinion(g, 1)


def add_negative_opinions(g: nx.Graph):
    """
    Add negative opinion (-1) to every agent.

    :param g: nx.Graph
    """
    _add_single_opinion(g, -1)


def has_opinion(g: nx.Graph) -> bool:
    """
    Check if `g` graph has `opinion` attribute

    :param g: nx.Graph
    :return: True if `g` has `opinion` attribute, False otherwise
    """
    if nx.get_node_attributes(g, 'opinion'):
        return True
    return False


def get_opinion_of_node(g, node):
    """
    Return opinion of given `node`

    :param g: nx.Graph
    :param node: node from nx.Graph
    :return: opinion: {-1, 1}
    """
    if not has_opinion(g):
        logger.error("Cannot get node opinion. Graph `g` has not attribute: `opinion`")
        return
    return g.nodes[node]['opinion']


def flip_opinion(g, node):
    """
    Flip opinion of given node (-1 => 1, 1 => -1)

    :param g: nx.Graph
    :param node: node from nx.Graph
    """
    if not has_opinion(g):
        logger.error("Cannot flip opinion. Graph `g` has not attribute: `opinion`")
        return
    g.nodes[node]['opinion'] = -1 if get_opinion_of_node(g, node) == 1 else 1


def _add_single_opinion(g: nx.Graph, value):
    for node in g.nodes():
        g.nodes[node]['opinion'] = value
