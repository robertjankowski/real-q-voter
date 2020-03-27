from src.real_q_voter.loader import *


def test_loader_empty_filename():
    assert load_graph('', 'example_graph') is None


def test_loader_wrong_format_type():
    assert load_graph('tests/test_graph.mtx', 'example_graph', format_type='wrong_format') is None


def test_loader_correct_graph():
    g = load_graph('tests/test_graph.mtx', 'example_graph')
    assert len(list(g.nodes())) > 0


def test_has_name():
    g = nx.complete_graph(2)
    assert has_name(g) is False
    add_graph_name(g, 'complete_graph')
    assert has_name(g) is True
