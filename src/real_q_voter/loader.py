import networkx as nx
import os

from src.real_q_voter.logger import get_logger

logger = get_logger('REAL-Q-VOTER-LOADER-LOGGER')


def load_graph(filename: str, graph_name: str, format_type='edge_list', is_directed=False):
    """
    Load directed or undirected graph from file with specific format

    :param filename: File to read graph
    :param graph_name: Graph name
    :param format_type: File format of saved graph e.g.: `edge_list`
    :param is_directed: Load as directed graph?
    :return: g: nx.Graph
    """
    if not os.path.isfile(filename):
        logger.error(f"File: [{filename}] does not exist")
        return

    if format_type == 'edge_list':
        graph_type = nx.DiGraph if is_directed else nx.Graph
        g = nx.read_edgelist(filename, create_using=graph_type)
        add_graph_name(g, graph_name)
        if nx.is_empty(g):
            logger.info("Loaded graph is empty")
        return g
    else:
        logger.error(f"Unknown graph input format: [{format_type}]")
        return


def add_graph_name(g: nx.Graph, name: str):
    """
    Add `name` attribute to graph

    :param g: nx.Graph
    :param name: Name of graph
    """
    g.graph['name'] = name


def has_name(g: nx.Graph) -> bool:
    """
    Check if given `g` graph has `name` attribute

    :param g: nx.Graph
    :return: True if `g` has `name`, False otherwise
    """
    if g.graph['name']:
        return True
    return False
