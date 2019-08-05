from pathlib import Path
import networkx as nx
import pandas as pd

graph_name = 'wikivote'
graph_type = 'di'
datasets_path = Path.cwd() / 'datasets'
graph_path = datasets_path / graph_name / str(graph_name + '.txt')


def get_graph_from_file():
    return nx.read_edgelist(graph_path, create_using=nx.Graph(), nodetype=int) if graph_type == 'un' \
        else nx.read_edgelist(graph_path, create_using=nx.DiGraph(), nodetype=int)


def increase_density(graph):
    density = nx.density(graph)
    core = [node for node, deg in nx.degree(graph) if deg >= 2]
    reduced_graph = nx.subgraph(graph, core)
    new_density = nx.density(reduced_graph)

    return reduced_graph if new_density > density else graph


def get_giant_connected_component(graph):
    gcc = [type(graph)(), "id"]
    scc = nx.strongly_connected_component_subgraphs(graph)
    for n_id, graph in enumerate(scc):
        if len(graph) > len(gcc[0]):
            gcc = [graph, "scc_" + str(n_id) + ".pickle"]

    nx.write_gpickle(gcc[0], path=gcc[1])
    return gcc


# Non mi convince molto
def get_eccentricity(graph):
    try:
        ecc = nx.eccentricity(type(graph)())
        return ecc
    except nx.exception.NetworkXError:  # Found infinite path length because the graph is not strongly connected
        eccentricity = []
        scc = nx.strongly_connected_component_subgraphs(graph)
        for n_id, graph in enumerate(scc):
            if len(graph) > 1:
                ecc = nx.eccentricity(graph)
                eccentricity.append((nx.center(scc, ecc), nx.periphery(scc, ecc),
                                     nx.radius(scc, ecc), nx.diameter(scc, ecc)))

    return eccentricity


def get_clustering_values(gcc, ego) -> tuple:
    clustering_coefficient = nx.clustering(gcc, ego)
    avg_clustering_coefficient = nx.average_clustering(gcc)
    transitivity = nx.transitivity(gcc)

    return clustering_coefficient, avg_clustering_coefficient, transitivity


def get_centralities(graph):
    return None
