from src.real_q_voter.opinion import *


def test_has_opinion():
    g = nx.complete_graph(5)
    assert has_opinion(g) is False
    add_random_opinions(g)
    assert has_opinion(g) is True


def test_positive_opinion():
    g = nx.complete_graph(5)
    add_positive_opinions(g)
    opinions = nx.get_node_attributes(g, 'opinion')
    assert all([opinion == 1 for opinion in opinions.values()])


def test_negative_opinion():
    g = nx.complete_graph(5)
    add_negative_opinions(g)
    opinions = nx.get_node_attributes(g, 'opinion')
    assert all([opinion == -1 for opinion in opinions.values()])


def test_get_opinion_of_node():
    g = nx.complete_graph(5)
    assert get_opinion_of_node(g, node=1) is None
    add_positive_opinions(g)
    assert get_opinion_of_node(g, node=1) is 1


def test_flip_opinion():
    g = nx.complete_graph(5)
    assert flip_opinion(g, 1) is None
    add_negative_opinions(g)
    [flip_opinion(g, node) for node in g.nodes]
    assert all([get_opinion_of_node(g, node) == 1 for node in g.nodes])
    [flip_opinion(g, node) for node in g.nodes]
    assert all([get_opinion_of_node(g, node) == -1 for node in g.nodes])
