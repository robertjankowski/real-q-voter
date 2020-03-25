import random

from src.real_q_voter.visualization import plot_network
from src.real_q_voter.loader import add_graph_name, has_name
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
    add_graph_name(g, 'ba')
    add_random_opinions(g)
    return g


def run(g: nx.Graph,
        q: int,
        p: float,
        eta=0.2,
        n_iteration=1000,
        preference_sampling=False,
        majority_conform=False,
        save_plot_graphs=False):
    """
    Perform simulation of q-voter model on `g` graph

    :param g: nx.Graph (directed or undirected)
    :param q: Number of agents in q-voter model
    :param p: Independence factor
    :param eta: Probability of conformity flip
    :param n_iteration: Number of simulation steps
    :param preference_sampling: Take into account degree of neighbours nodes while sampling for `q` nodes
    :param majority_conform: True: In conformity state use majority votes of neighbors.
        False: All agents should have the same opinions.
    :param save_plot_graphs: If save plot of network on each iteration

    :return: (mean_opinions: list, weighted_mean_opinions: list)
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
            _act_independently(g, node)
        else:
            _act_conform(g, node, q, eta, preference_sampling, majority_conform)
        mean_opinions.append(calculate_mean_opinion(g))
        weighted_mean_opinions.append(calculate_weighted_mean_opinion(g))
        if save_plot_graphs and has_name(g):
            _save_plot_graphs(i, n_iteration, g, p, q)
    return mean_opinions, weighted_mean_opinions


def _save_plot_graphs(i, n_iteration, g: nx.Graph, p: float, q: int):
    # Save only 10 frames (network plots)
    by = n_iteration / 10
    if i % by == 0:
        graph_name = g.graph['name']
        iteration = str(i).zfill(len(str(n_iteration)))
        title = f"{graph_name}_p={round(p, 3)}_q={q}/{graph_name}_q={q}_p={round(p, 3)}_i={iteration}"
        plot_network(g, title=title, show_opinion=True, filename=title)


def _act_independently(g: nx.Graph, node):
    if np.random.rand() < 0.5:
        flip_opinion(g, node)


def _act_conform(g: nx.Graph, node, q: int, eta: float, preference_sampling: bool, majority_conform: bool):
    neighbours = _get_neighbours_from_node(g, node, q, preference_sampling)
    if _check_majority_conform(g, neighbours, majority_conform):
        g.nodes[node]['opinion'] = get_opinion_of_node(g, neighbours[0])
    else:
        if np.random.rand() < eta:
            flip_opinion(g, node)


def _get_neighbours_from_node(g: nx.Graph, node, q: int, preference_sampling: bool):
    """
    Return `q` neighbours of given `node` with/without degree preferences.

    :param g: nx.Graph
    :param node: node from nx.Graph
    :param q: number of neighbours
    :param preference_sampling: Take into account degree of neighbours nodes while sampling for `q` nodes
    :return: `q` neighbours
    """
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
    return neighbours


def _check_majority_conform(g: nx.Graph, neighbours, majority_conform: bool):
    """
    Check if all or majority of neighbours has the same opinion

    :param g: nx.Graph
    :param neighbours: `q` neighbours
    :param majority_conform: Use majority of votes?
    :return: True if all/majority have the same opinion, False otherwise
    """
    neighbours_opinions = [get_opinion_of_node(g, n) for n in neighbours]
    neighbours_opinions_total = sum(neighbours_opinions)
    if not majority_conform:
        is_conformity_neighbour = neighbours_opinions_total == len(neighbours_opinions) \
                                  or neighbours_opinions_total == -len(neighbours_opinions)
    else:
        is_conformity_neighbour = neighbours_opinions_total > len(neighbours_opinions) / 2 \
                                  or neighbours_opinions_total < -len(neighbours_opinions) / 2
    return is_conformity_neighbour


def _get_nodes_with_most_degree(neighbours, g: nx.Graph):
    """
    Return sorted neighbours by their degree (hubs are first).

    :param neighbours: nodes from nx.Graph
    :param g: nx.Graph
    :return: sorted neighbours
    """
    neighbours_degrees = g.degree(neighbours)
    sorted_neighbours = sorted(neighbours_degrees, key=lambda x: x[1], reverse=True)
    return list(map(lambda x: x[0], sorted_neighbours))
