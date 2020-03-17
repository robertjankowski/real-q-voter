from real_q_voter.metrics import *
from real_q_voter.simulation import *
from real_q_voter.visualization import *
from real_q_voter.loader import *


def main():
    g = load_graph("../../data/soc-wiki-Vote.mtx", is_directed=True)
    add_random_opinions(g)
    # plot_network(g, node_color='red')

    # ba = ba_graph_with_opinion(10000)
    # print(calculate_weighted_mean_opinion(ba))

    mean_opinions, weighted_opinions = run(g, 3, 0.2)
    plt.plot(weighted_opinions)
    plt.show()
    # plot_degree_distribution(ba, bins=30)


if __name__ == "__main__":
    main()
