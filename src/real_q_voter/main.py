from src.real_q_voter.simulation import *
from src.real_q_voter.visualization import *


def run_simulation(g: nx.Graph, q: int, p_range: list, n_iteration: int, save_plot_graphs=False):
    mean_opinions = []
    weighted_mean_opinions = []
    for p in p_range:
        add_positive_opinions(g)
        mean_opinion, weighted_mean_opinion = run(g, q, p, n_iteration=n_iteration,
                                                  save_plot_graphs=save_plot_graphs)
        mean_opinions.append(mean_opinion)
        weighted_mean_opinions.append(weighted_mean_opinion)
    return mean_opinions, weighted_mean_opinions


def main():
    # g = load_graph("../../data/soc-wiki-Vote.mtx", graph_name='soc-wiki-Vote', is_directed=False)
    # add_random_opinions(g)

    p_range = np.arange(0.0, 0.5, 0.01)
    ba = ba_graph_with_random_opinion(100)
    mean_opinions, weighted_mean_opinions = run_simulation(ba, 4, p_range, 5000, save_plot_graphs=False)
    m = [np.mean(m) for m in mean_opinions]
    w = [np.mean(w) for w in weighted_mean_opinions]
    plt.plot(p_range, m, label='mean_opinion')
    plt.plot(p_range, w, label='weighted_mean_opinion')
    plt.legend()
    plt.show()
    # convert_images_to_gif("../../figures/ba_p=0.4/*.png", 'test')


if __name__ == "__main__":
    main()
