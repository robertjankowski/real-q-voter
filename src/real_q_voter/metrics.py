import networkx as nx
import numpy as np

from src.real_q_voter.opinion import has_opinion
from src.real_q_voter.logger import get_logger

logger = get_logger('REAL-Q-VOTER-METRICS-LOGGER')


def calculate_mean_opinion(g: nx.Graph):
    """
    Calculate mean opinion <s> of the nodes in graph

    :param g: nx.Graph
    :return: mean opinion: float
    """
    if not has_opinion(g):
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
    if not has_opinion(g):
        logger.error("Cannot calculate weighted mean opinion. Graph `g` has not attribute: `opinion`")
        return
    weights = []
    opinions = []
    for node in g.nodes():
        opinion = g.nodes[node]['opinion']
        weight = g.degree[node]
        weights.append(weight)
        if isinstance(opinion, np.ndarray):
            opinion = opinion[0]
        opinions.append(opinion)
    return np.average(np.array(opinions), weights=np.array(weights))
