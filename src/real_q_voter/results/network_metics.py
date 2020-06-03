import networkx as nx
import pandas as pd
import numpy as np


def metrics_report(g: nx.Graph):
    C = nx.average_clustering(g)
    knn = np.mean(np.array(list(dict(nx.average_neighbor_degree(g)).values())))
    k = np.mean(np.array(list(dict(g.degree).values())))
    E = g.number_of_edges()
    N = g.number_of_nodes()
    l = nx.average_shortest_path_length(g)
    return pd.DataFrame(data={'C': C, 'k_nn': knn, 'k': k, 'E': E, 'N': N, 'l': l}, index=[0])


def load_network(filename) -> nx.Graph:
    return nx.read_edgelist(f'../../../data/{filename}')


def main():
    moreno_health = load_network('moreno_health.edges')
    socfb = load_network('socfb-Stanford3.mtx')
    routers = load_network('tech-routers-rf.mtx')
    print('Network loaded...')
    moreno_health_metrics = metrics_report(moreno_health)
    print('Finished moreno')
    socfb_metrics = metrics_report(socfb)
    print('Finished socfb')
    routers_metrics = metrics_report(routers)
    print('Finished routers')
    all_metrics = pd.concat(
        [moreno_health_metrics, socfb_metrics, routers_metrics])
    print(all_metrics.to_markdown())
    all_metrics.to_csv('network_metrics_table.csv', index=False)


if __name__ == "__main__":
    main()
