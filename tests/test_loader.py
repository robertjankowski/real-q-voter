from src.real_q_voter.loader import *


def test_loader_empty_filename():
    assert load_graph('') is None


def test_loader_wrong_format_type():
    assert load_graph('tests/test_graph.mtx', format_type='wrong_format') is None


def test_loader_correct_graph():
    g = load_graph('tests/test_graph.mtx')
    assert len(list(g.nodes())) > 0
