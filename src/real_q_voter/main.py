from real_q_voter.metrics import *
from real_q_voter.simulation import *
from real_q_voter.visualization import *
from real_q_voter.loader import *


def main():
    g = load_graph("../../data/soc-wiki-Vote.mtx", is_directed=True)
    add_random_opinions(g)
    plot_network(g, node_color='red')

    ba = ba_graph(1e3, 4)
    print(calculate_weighted_mean_opinion(ba))

    plot_degree_distribution(ba, bins=30)


if __name__ == "__main__":
    main()
