from pathlib import Path
from networkx import Graph, DiGraph, read_edgelist


graph_name= 'amazon'
graph_type = 'un'
datasets_path = Path.cwd() / 'datasets'
graph_path = datasets_path / graph_name / str(graph_name + '.txt')


def get_graph_from_file():
    return read_edgelist(graph_path, create_using=Graph(), nodetype=int) if graph_type == 'un' \
        else read_edgelist(graph_path, create_using=DiGraph(), nodetype=int)
