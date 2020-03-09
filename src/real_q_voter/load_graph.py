import matplotlib.pyplot as plt
import networkx as nx


def main():
    g = nx.read_edgelist("../../data/soc-wiki-Vote.mtx")

    degrees = list(map(lambda x: x[1], g.degree()))
    plt.hist(degrees)
    plt.xscale('log')
    plt.yscale('log')

    # nx.draw(g)
    plt.show()


if __name__ == "__main__":
    main()
