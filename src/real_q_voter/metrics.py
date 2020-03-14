import networkx as nx
import numpy as np
import logging

logger = logging.getLogger('REAL-Q-VOTER-METRICS-LOGGER')


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