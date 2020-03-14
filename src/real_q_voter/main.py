from src.real_q_voter.metrics import *
from src.real_q_voter.simulation import *
from src.real_q_voter.visualization import *


def main():
    # NOTE: Should I use Directed or Undirected Graph ->
    #  then I have to use input and output degree in mean weighted opinion
    # g.in_degree <-> g.degree
    g = nx.read_edgelist("../../data/soc-wiki-Vote.mtx", create_using=nx.DiGraph)
    add_random_opinions(g)
    plot_network(g, node_color='red')

    ba = ba_graph(1e3, 4)
    print(calculate_weighted_mean_opinion(ba))

    plot_degree_distribution(ba, bins=30)


if __name__ == "__main__":
    main()
