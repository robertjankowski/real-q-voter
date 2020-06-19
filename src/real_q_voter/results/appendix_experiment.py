import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rc('text', usetex=True)
matplotlib.rc('font', size=15)
matplotlib.rc('legend', fontsize=14)


def plot_results(pathA, pathB, title=None, filename=None, pdf=False):
    dataA = pd.read_csv(pathA)
    dataB = pd.read_csv(pathB)

    p_range = pd.to_numeric(dataA.columns)
    statsA = dataA.apply(lambda x: (np.mean(x), np.std(x)))
    mean_opinionA, std_opinionA = list(zip(*statsA.values))

    statsB = dataB.apply(lambda x: (np.mean(x), np.std(x)))
    mean_opinionB, std_opinionB = list(zip(*statsB.values))

    plt.errorbar(p_range,
                 mean_opinionA,
                 yerr=std_opinionA,
                 fmt='o',
                 color='blue',
                 label='without preference sampling')
    plt.errorbar(p_range,
                 mean_opinionB,
                 yerr=std_opinionB,
                 fmt='o',
                 color='red',
                 label='with preference sampling')

    plt.ylabel(r'$m(p)$')
    plt.xlabel(r'$p$')
    plt.grid(alpha=0.3)
    plt.legend()
    if title:
        plt.plot(title)

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
    plot_results(
        '../../../results/directed-undirected-appendix/moreno_is_random=False_I=10_directed=False_q=4_N=25390.csv',
        '../../../results/directed-undirected-appendix/moreno_preference_sampling=True_is_random=False_I=10_directed=False_q=4_N=25390.csv',
        filename='moreno_preference_sampling_appendix_start_ones',
        pdf=True)


if __name__ == '__main__':
    main()
