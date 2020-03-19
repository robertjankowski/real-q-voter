import random

from src.real_q_voter.metrics import *
from src.real_q_voter.opinion import *


def ba_graph_with_random_opinion(n, m=8) -> nx.Graph:
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
        preference_sampling=False,
        majority_conformity=False):
    """
    Perform simulation of q-voter model on `g` graph

    :param g: nx.Graph (directed or undirected)
    :param q: Number of agents in q-voter model
    :param p: Independence factor
    :param eta: Probability of conformity flip
    :param n_iteration: Number of simulation steps
    :param preference_sampling: Take into account degree of neighbours nodes while sampling for `q` nodes
    :param majority_conformity: True: In conformity state use majority votes of neighbors.
        False: All agents should have the same opinions.

    :return: (mean_opinions: list, weighted_mean_opinion: list)
    """
    if not has_opinion(g):
        logger.error("Cannot run simulation. Graph `g` has not attribute: `opinion`")
        return
    mean_opinions = []
    weighted_mean_opinions = []
    nodes = list(g.nodes)
    for _ in range(n_iteration):
        node = random.choice(nodes)
        if np.random.rand() < p:
            # Act independently
            if np.random.rand() < 0.5:
                flip_opinion(g, node)
        else:
            # Conformity
            neighbours = list(g.neighbors(node))
            if preference_sampling:
                neighbours = _get_nodes_with_most_degree(neighbours, g)
            if len(neighbours) > q:
                neighbours = neighbours[:q]
            while len(neighbours) < q:
                # Add neighbour of neighbour
                node_neighbour = random.choice(neighbours)
                node_neighbour = list(g.neighbors(node_neighbour))
                node_neighbour = random.choice(node_neighbour)
                if node_neighbour != node:
                    neighbours.append(node_neighbour)

            neighbours_opinions = [get_opinion_of_node(g, n) for n in neighbours]
            neighbours_opinions_total = sum(neighbours_opinions)

            if not majority_conformity:
                is_conformity_neighbour = neighbours_opinions_total == len(neighbours_opinions) \
                                          or neighbours_opinions_total == -len(neighbours_opinions)
            else:
                is_conformity_neighbour = neighbours_opinions_total > len(neighbours_opinions) / 2 \
                                          or neighbours_opinions_total < -len(neighbours_opinions) / 2
            if is_conformity_neighbour:
                g.nodes[node]['opinion'] = get_opinion_of_node(g, neighbours[0])
            else:
                if np.random.rand() < eta:
                    flip_opinion(g, node)

        mean_opinions.append(calculate_mean_opinion(g))
        weighted_mean_opinions.append(calculate_weighted_mean_opinion(g))
    return mean_opinions, weighted_mean_opinions


def _get_nodes_with_most_degree(neighbours, g: nx.Graph):
    neighbours_degrees = g.degree(neighbours)
    sorted_neighbours = sorted(neighbours_degrees, key=lambda x: x[1], reverse=True)
    return list(map(lambda x: x[0], sorted_neighbours))
