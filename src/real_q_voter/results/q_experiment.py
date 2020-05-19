from src.real_q_voter.results.utils import *

import matplotlib.pyplot as plt


def plot_by_dataset(q: int, with_weighted_opinion=False, filename=None):
    files = filter_files_by(fetch_files_from("q-experiment"), f'q={q}')
    plot_experiment(files, with_weighted_opinion)
    plt.title(f'q-experiment for q={q}')
    if filename:
        plt.savefig(f'../../../figures/{filename}.png', bbox_inches='tight', dpi=400)
    else:
        plt.show()


def plot_by_q(dataset: str, with_weighted_opinion=False, filename=None):
    files = filter_files_by(fetch_files_from("q-experiment"), dataset)
    plot_experiment(files, with_weighted_opinion, show_q=True)
    plt.title(f'q-experiment for dataset={dataset}')
    if filename:
        plt.savefig(f'../../../figures/{filename}.png', bbox_inches='tight', dpi=400)
    else:
        plt.show()


def main():
    plot_by_q("ba", with_weighted_opinion=True)
    plot_by_dataset(3, with_weighted_opinion=True)
    plot_by_q("soc-fb", with_weighted_opinion=True)


if __name__ == '__main__':
    main()
