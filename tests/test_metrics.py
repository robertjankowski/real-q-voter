from src.real_q_voter.metrics import *
from src.real_q_voter.opinion import *


def test_metrics_without_opinion():
    g = nx.Graph([(1, 2), (2, 3)])
    assert calculate_mean_opinion(g) is None
    assert calculate_weighted_mean_opinion(g) is None


def test_mean_opinion():
    g = nx.complete_graph(10)
    add_positive_opinions(g)
    assert calculate_mean_opinion(g) == 1
    add_negative_opinions(g)
    assert calculate_mean_opinion(g) == -1


def test_weighted_mean_opinion():
    g = nx.complete_graph(10)
    add_positive_opinions(g)
    assert calculate_weighted_mean_opinion(g) == 1
