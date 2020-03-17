from real_q_voter.metrics import *
import random
import logging

logger = logging.getLogger('REAL-Q-VOTER-SIMULATION-LOGGER')


def add_random_opinions(g: nx.Graph):
    """
    Initialize nodes of a graph with randomly generated opinions [-1, 1]

    :param g: nx.Graph
    """
    for node in g.nodes():
        g.nodes[node]['opinion'] = np.random.choice([0, 1], 1)


def ba_graph_with_opinion(n, m=5) -> nx.Graph:
    """
    Construct BA network with randomly generated opinions

    :param n: Number of nodes
    :param m: Number of edges to attach from a new node to existing nodes
    :return: nx.Graph with opinion attribute
    """
    g = nx.barabasi_albert_graph(n, m)
    add_random_opinions(g)
    return g


def run(g: nx.Graph,
        q: int,
        p: float,
        eta: float = 0.2,
        n_iteration: int = 1000,
        preference_sampling=False):
    """
    Perform simulation of q-voter model on `g` graph

    :param g: nx.Graph (directed or undirected)
    :param q: Number of agents in q-voter model
    :param p: Independence factor
    :param eta: Probability of conformity flip
    :param n_iteration: Number of simulation steps
    :param preference_sampling: Take into account degree of neighbours nodes while sampling for `q` nodes
    :return:
    """
    if not has_opinion(g):
        logger.error("Cannot run simulation. Graph `g` has not attribute: `opinion`")
        return
    mean_opinions = []
    weighted_mean_opinions = []
    nodes = list(g.nodes)
    for i in range(n_iteration):
        node = random.choice(nodes)
        if np.random.rand() < p:
            # Act independently
            if np.random.rand() < 0.5:
                _flip_opinion(g, node)
        else:
            # Conformity
            # TODO: add preference sampling using degree of neighbours nodes.
            neighbours = list(g.neighbors(node))
            if len(neighbours) > q:
                neighbours = neighbours[:q]
            while len(neighbours) < q:
                node_neighbour = random.choice(neighbours)
                if node_neighbour != node:
                    neighbours.append(node_neighbour)

            neighbours_opinions = [_get_opinion_of_node(g, n) for n in neighbours]
            # TODO: add majority options
            neighbours_opinions_total = sum(neighbours_opinions)
            if neighbours_opinions_total == len(neighbours_opinions) \
                    or neighbours_opinions_total == 0:  # the same opinion
                g.nodes[node]['opinion'] = _get_opinion_of_node(g, neighbours[0])
            else:
                if np.random.rand() < eta:
                    _flip_opinion(g, node)

        mean_opinions.append(calculate_mean_opinion(g))
        weighted_mean_opinions.append(calculate_weighted_mean_opinion(g))
    return mean_opinions, weighted_mean_opinions


def _get_opinion_of_node(g, node):
    if not has_opinion(g):
        logger.error("Cannot get node opinion. Graph `g` has not attribute: `opinion`")
        return
    return g.nodes[node]['opinion']


def _flip_opinion(g, node):
    g.nodes[node]['opinion'] = 0 if _get_opinion_of_node(g, node) else 1
