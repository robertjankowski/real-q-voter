import networkx as nx
import numpy as np
import pandas as pd

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
        logger.error(
            "Cannot calculate mean opinion. Graph `g` has not attribute: `opinion`")
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
        logger.error(
            "Cannot calculate weighted mean opinion. Graph `g` has not attribute: `opinion`")
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


def save_metrics(filename: str, p_range: list, mean_opinions: list = None, weighted_mean_opinions: list = None):
    """
    Save to file opinions metrics

    :param filename: Name of file
    :param p_range: Independence factor range
    :param mean_opinions: List of list per single `p` values
    :param weighted_mean_opinions: List of list per single `p` values
    """
    base_path = '../../output/'
    if mean_opinions:
        df_mean_opinion = pd.DataFrame(mean_opinions).transpose()
        df_mean_opinion.columns = p_range
        print(base_path + filename + '_mean_opinion.csv')
        df_mean_opinion.to_csv(base_path + filename +
                               '_mean_opinion.csv', index=False)
    if weighted_mean_opinions:
        df_weighted_mean_opinion = pd.DataFrame(
            weighted_mean_opinions).transpose()
        df_weighted_mean_opinion.columns = p_range
        df_weighted_mean_opinion.to_csv(
            base_path + filename + '_weighted_mean_opinion.csv', index=False)


def read_metrics(filename: str):
    """
    Read (mean opinions or weighted mean opinions) metrics from file

    :param filename: Name of the file
    :return: (p_range, opinions)
    """
    opinions = []
    df = pd.read_csv(filename)
    for col in df.columns:
        opinions.append(df[col].values)
    p_range = df.columns.astype('float').values
    return p_range, opinions
