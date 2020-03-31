import os
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import glob
from src.real_q_voter.logger import get_logger
from itertools import accumulate
from PIL import Image

logger = get_logger('REAL-Q-VOTER-VISUALIZATION-LOGGER')


def plot_degree_distribution(g: nx.Graph, bins=50, filename=None, file_extension='png'):
    """
    Plot degree distribution of given `g` graph.

    :param g: nx.Graph (directed or undirected)
    :param bins: number of bins for histogram
    :param filename: Name of the output figure
    :param file_extension: Extension of the output plot
    """
    fig, ax = plt.subplots()

    if nx.is_directed(g):
        in_degrees, out_degrees = _extract_degrees_from_graph(g, is_directed=True)
        in_degrees = np.histogram(in_degrees, bins=bins, density=True)
        out_degrees = np.histogram(out_degrees, bins=bins, density=True)
        ax.loglog(in_degrees[1][:-1], in_degrees[0], label='in_degree')
        ax.loglog(out_degrees[1][:-1], out_degrees[0], label='out_degree')
        ax.legend()
    else:
        degrees = _extract_degrees_from_graph(g)
        degrees = np.histogram(degrees, bins=bins, density=True)
        ax.loglog(degrees[1][:-1], degrees[0])
    ax.set_xlabel('k')
    ax.set_ylabel('P(k)')
    ax.tick_params(which="minor", axis="x", direction="in")
    ax.tick_params(which="minor", axis="y", direction="in")
    ax.tick_params(which="major", axis="x", direction="in")
    ax.tick_params(which="major", axis="y", direction="in")

    if filename:
        _save_plot_as('../../figures/' + filename, file_extension)
    else:
        plt.show()


def plot_network(g: nx.Graph, title='', show_opinion=False, filename=None, file_extension='png', **plot_parameters):
    """
    Plot `g` network

    :param g: nx.Graph
    :param title: Title of graph
    :param show_opinion: Color network by opinion?
    :param filename: Name of the output figure
    :param file_extension: Extension of the output plot
    """
    opinions = None
    if show_opinion:
        opinions = np.array(list(nx.get_node_attributes(g, 'opinion').values()))
        opinions = ['red' if opinion == 1 else 'blue' for opinion in opinions]

    nx.draw(g, pos=nx.spring_layout(g, seed=42), node_color=opinions,
            node_size=30, edge_color=[0, 0, 0, 0.2], alpha=0.6,
            cmap=plt.cm.jet, **plot_parameters)
    plt.title(title)

    if filename:
        base_path = '../../figures/'
        _create_folders(base_path, filename)
        _save_plot_as(base_path + filename, file_extension)
        plt.close()
    plt.show()


def plot_mean_opinion_independence_factor(p_range: list, mean_opinions: list, weighted_mean_opinions: list,
                                          filename=None, file_extension='png'):
    """
    Plot relationship between independence factor and mean opinions

    :param p_range: Range of `p` independence factor
    :param mean_opinions: List of lists mean opinions
    :param weighted_mean_opinions: List of lists weighted opinion
    :param filename: Name of the output figure
    :param file_extension: Extension of the output plot
    """
    m = [np.mean(m) for m in mean_opinions]
    w = [np.mean(w) for w in weighted_mean_opinions]
    plt.plot(p_range, m, label='mean opinion')
    plt.plot(p_range, w, label='weighted mean opinion')
    plt.xlabel('p')
    plt.ylabel(r'$\left<s\right>$')
    plt.legend()
    if filename:
        _save_plot_as('../../figures/' + filename, file_extension)
    else:
        plt.show()


def convert_images_to_gif(input_path: str, output_name: str):
    """
    Convert images into gif

    :param input_path: Input path e.g. `../figures/*.png`
    :param output_name: Output gif name in input_path directory
    """
    output_path = '/'.join(input_path.split('/')[:-1]) + '/' + output_name + '.gif'
    img, *imgs = [Image.open(f) for f in sorted(glob.glob(input_path))]
    img.save(fp=output_path, format='GIF', append_images=imgs,
             save_all=True, duration=400, loop=0)


def _create_folders(base_path: str, filename: str):
    folders_names = filename.split('/')[:-1]
    folders_names = [folder + '/' for folder in folders_names]
    folders_names = list(accumulate(folders_names))
    folders = [base_path + folder for folder in folders_names]
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)


def _extract_degrees_from_graph(g: nx.Graph, is_directed=False):
    if is_directed:
        in_degrees = list(map(lambda x: x[1], g.in_degree))
        out_degrees = list(map(lambda x: x[1], g.out_degree))
        return in_degrees, out_degrees
    else:
        degrees = list(map(lambda x: x[1], g.degree))
        return degrees


def _save_plot_as(filename: str, extension: str):
    if extension is 'png':
        plt.savefig(filename + '.png', bbox_inches='tight', dpi=400)
    elif extension is 'pdf':
        plt.savefig(filename + '.pdf')
    else:
        logger.error('Cannot save plot. Unsupported extension')
    plt.close()
