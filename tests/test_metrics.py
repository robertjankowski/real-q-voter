from src.real_q_voter.metrics import *


def test_metrics_without_opinion():
    g = nx.Graph([(1, 2), (2, 3)])
    assert calculate_mean_opinion(g) is None
    assert calculate_weighted_mean_opinion(g) is None
