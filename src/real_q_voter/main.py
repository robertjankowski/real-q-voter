from src.real_q_voter.simulation import *
from src.real_q_voter.visualization import *


def main():
    # g = load_graph("../../data/soc-wiki-Vote.mtx", is_directed=False)
    # add_random_opinions(g)

    m_opinion = []
    w_opinion = []
    p_range = np.arange(0, 0.6, 0.1)
    ba = ba_graph_with_random_opinion(100)
    plot_network(ba, show_opinion=True)
    for p in p_range:
        add_positive_opinions(ba)
        mean_opinions, weighted_opinions = run(ba, 4, p=p, n_iteration=5000)
        m_opinion.append(np.mean(mean_opinions))
        w_opinion.append(np.mean(weighted_opinions))

    plt.plot(p_range, m_opinion, label='mean_opinion')
    plt.plot(p_range, w_opinion, label='weighted_mean_opinion')
    plt.legend()
    plt.show()
    plot_network(ba, show_opinion=True)


if __name__ == "__main__":
    main()
