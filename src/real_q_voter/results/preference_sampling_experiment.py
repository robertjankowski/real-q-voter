from src.real_q_voter.results.utils import *


def plot_preference_sampling_experiment(with_weighted_opinion=False, q=None, filename=None):
    with_preference_files = fetch_files_from("preference-sampling-experiment")
    without_preference_files = filter_files_by(fetch_files_from("q-experiment"), 'soc-fb')
    if q:
        with_preference_files = filter_files_by(with_preference_files, f'q={q}')
        without_preference_files = filter_files_by(without_preference_files, f'q={q}')
    plot_experiment(with_preference_files, with_weighted_opinion, show_q=True)
    plot_experiment(without_preference_files, with_weighted_opinion, show_q=True)
    if filename:
        plt.savefig(f'../../../figures/{filename}.png', bbox_inches='tight', dpi=400)
    else:
        plt.show()


def main():
    plot_preference_sampling_experiment(q=3, filename='preference_sampling_q_3')


if __name__ == '__main__':
    main()
