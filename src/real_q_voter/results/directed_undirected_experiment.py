from utils import *

import matplotlib.pyplot as plt


def plot_by_dataset(q: int, with_weighted_opinion=False, filename=None, pdf=False):
    files = filter_files_by(fetch_files_from(
        "directed-undirected-experiment"), f'q={q}')
    plot_experiment(files, with_weighted_opinion)
    plt.title(f'directed-undirected-experiment for q={q}')
    if filename:
        if pdf:
            plt.savefig(
                f'../../../figures/{filename}.pdf', bbox_inches='tight')
        else:
            plt.savefig(
                f'../../../figures/{filename}.png', bbox_inches='tight', dpi=400)
        plt.close()
    else:
        plt.show()


def plot_by_q(dataset: str, with_weighted_opinion=False, filename=None, pdf=False):
    files = filter_files_by(fetch_files_from(
        "directed-undirected-experiment"), dataset)
    plot_experiment(files, with_weighted_opinion, show_q=True)
    plt.title(f'directed-undirected-experiment for dataset={dataset}')
    if filename:
        if pdf:
            plt.savefig(
                f'../../../figures/{filename}.pdf', bbox_inches='tight')
        else:
            plt.savefig(
                f'../../../figures/{filename}.png', bbox_inches='tight', dpi=400)
        plt.close()
    else:
        plt.show()


def main():
    plot_by_q("health", with_weighted_opinion=False,
              filename='directed_undirected_all', pdf=True)
    # plot_by_dataset(2, with_weighted_opinion=True,
    #                 filename='directed_undirected_q=2', pdf=False)
    # plot_by_dataset(3, with_weighted_opinion=True,
    #                 filename='directed_undirected_q=3', pdf=False)
    # plot_by_dataset(4, with_weighted_opinion=True,
    #                 filename='directed_undirected_q=4', pdf=False)


if __name__ == '__main__':
    main()
