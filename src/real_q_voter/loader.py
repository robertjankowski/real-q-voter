import networkx as nx
import os

from src.real_q_voter.logger import get_logger

logger = get_logger('REAL-Q-VOTER-LOADER-LOGGER')


def load_graph(filename: str, format_type: str = 'edge_list', is_directed=False):
    """
    Load directed or undirected graph from file with specific format

    :param filename: File to read graph
    :param format_type: File format of saved graph e.g.: `edge_list`
    :param is_directed: Load as directed graph?
    :return: g: nx.Graph
    """
    if not os.path.isfile(filename):
        logger.error(f"File: [{filename}] does not exists")
        return

    if format_type == 'edge_list':
        graph_type = nx.DiGraph if is_directed else nx.Graph
        g = nx.read_edgelist(filename, create_using=graph_type)
        if _is_empty_graph(g):
            logger.info("Loaded graph is empty")
        return g
    else:
        logger.error(f"Unknown graph input format: [{format_type}]")
        return


def _is_empty_graph(g: nx.Graph) -> bool:
    return nx.is_empty(g)
