from utils import get_graph_from_file, increase_density, get_giant_connected_component, get_eccentricity, \
    get_clustering_values, get_centralities

if __name__ == '__main__':
    graph = get_graph_from_file()

    '''
    
    gcc = get_giant_connected_component(graph)
    print(gcc)
    
    ecc = get_eccentricity(graph)
    print(ecc)
    
    cc_val = get_clustering_values(graph)
    print(cc_val[0], cc_val[1], cc_val[2])
    
    
    '''