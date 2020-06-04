from utils import *


def plot_preference_sampling_experiment(with_weighted_opinion=False, q=None, filename=None, pdf=False):
    with_preference_files = fetch_files_from("preference-sampling-experiment")
    without_preference_files = filter_files_by(fetch_files_from("q-experiment"), 'soc-fb')
    if q:
        with_preference_files = filter_files_by(with_preference_files, f'q={q}')
        without_preference_files = filter_files_by(without_preference_files, f'q={q}')
    plot_experiment(with_preference_files, with_weighted_opinion, show_q=True)
    plot_experiment(without_preference_files, with_weighted_opinion, show_q=True)
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
    plot_preference_sampling_experiment(q=2, filename='preference_sampling_q_2', pdf=False)
    plot_preference_sampling_experiment(q=3, filename='preference_sampling_q_3', pdf=False)
    plot_preference_sampling_experiment(q=4, filename='preference_sampling_q_4', pdf=False)

if __name__ == '__main__':
    main()
