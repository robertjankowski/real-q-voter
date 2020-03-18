from real_q_voter.simulation import *
from real_q_voter.visualization import *


def main():
    # g = load_graph("../../data/soc-wiki-Vote.mtx", is_directed=True)
    # add_random_opinions(g)
    # plot_network(g, node_color='red')

    m_opinion = []
    w_opinion = []
    p_range = np.arange(0, 0.6, 0.1)
    ba = ba_graph_with_random_opinion(1000)
    for p in p_range:
        add_positive_opinions(ba)
        mean_opinions, weighted_opinions = run(ba, 4, p=p, n_iteration=5000)
        m_opinion.append(np.mean(mean_opinions))
        w_opinion.append(np.mean(weighted_opinions))

    plt.plot(p_range, m_opinion, label='mean_opinion')
    plt.plot(p_range, w_opinion, label='weighted_mean_opinion')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
