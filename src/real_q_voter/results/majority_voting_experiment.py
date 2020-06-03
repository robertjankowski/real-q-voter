from utils import *


def plot_majority_voting_experiment(with_weighted_opinion=False, q=None, filename=None, pdf=False):
    with_majority_files = fetch_files_from("majority-voting-experiment")
    without_majority_files = filter_files_by(
        fetch_files_from("q-experiment"), 'soc-fb')[1:]
    if q:
        with_majority_files = filter_files_by(with_majority_files, f'q={q}')
        without_majority_files = filter_files_by(
            without_majority_files, f'q={q}')
    plot_experiment(with_majority_files, with_weighted_opinion, show_q=True)
    plot_experiment(without_majority_files, with_weighted_opinion, show_q=True)
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
    plot_majority_voting_experiment(filename='majority_voting_all', pdf=True)


if __name__ == '__main__':
    main()
