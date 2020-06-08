import glob
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.colors as mcolors
import random

matplotlib.rc('text', usetex=True)
matplotlib.rc('font', size=15)
matplotlib.rc('legend', fontsize=14)


def read_metrics(filename: str):
    opinions = []
    df = pd.read_csv(filename)
    for col in df.columns:
        opinions.append(df[col].values)
    p_range = df.columns.astype('float').values
    return p_range, opinions


def filter_files_by(files: list, query: str):
    return [f for f in files if query in f]


def plot_experiment(files, with_weighted_opinion=False, show_q=False, col=None):
    colors = list(dict(mcolors.TABLEAU_COLORS).values())
    colors.insert(0, 'k')
    colors.append('lime')
    for i, f in enumerate(files):
        result = pd.read_csv(f)
        opinion_type = extract_opinion_type(f)
        if not with_weighted_opinion and 'weighted_mean_opinion' in opinion_type:
            continue
        result.columns = ['p_range', opinion_type]
        plot_label = extract_name(f) + ' ' + opinion_type.replace('_', ' ')
        plot_label = plot_label.split('/')[-1]
        if show_q:
            plot_label += ' ' + extract_q(f)
        plt.grid(alpha=0.3)
        if col:
            colors[i] = col
        plt.scatter(result['p_range'], result[opinion_type],
                    color=colors[i])
        plt.plot(result['p_range'], result[opinion_type],
                 color=colors[i], alpha=0.6)
        plt.plot([], [], '-o', label=plot_label, color=colors[i])

    plt.xlabel('p')
    plt.ylabel('opinion')
    plt.legend()


def extract_q(file: str):
    q = re.search(r'q=\d', file)
    return q.group(0)


def extract_opinion_type(file: str):
    opinion_type = re.search(r'\D+opinion', file)
    return opinion_type.group(0)[1:]


def extract_name(file: str):
    return file.split('\\')[-1].split('-q')[0].replace('_', ' ')


def fetch_files_from(experiment: str):
    return glob.glob(f"../../../results/{experiment}/*.txt")


def convert_old_format_results(path):
    """
    Convert old `.csv` format into simple p_range, mean_opinion dataframe

    :param path:
    """
    files = glob.glob(path)

    for f in files:
        p_range, opinion = read_metrics(f)
        opinion = np.transpose(opinion)[-1]  # last opinion from simulation
        df = pd.DataFrame(data={'p_range': p_range, 'opinion': opinion})
        save_file = f.split('.csv')[0]
        save_file = save_file + '.txt'
        df.to_csv(save_file, index=False, header=False)


if __name__ == '__main__':
    # convert_old_format_results("../../../new_results/q-experiment/*.csv")
    # convert_old_format_results("../../../new_results/preference-sampling-experiment/*.csv")
    # convert_old_format_results("../../../new_results/majority-voting-experiment/*.csv")
    convert_old_format_results(
        "../../../new_results/directed-undirected-experiment/*.csv")
