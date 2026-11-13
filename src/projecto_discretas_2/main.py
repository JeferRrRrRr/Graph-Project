from projecto_discretas_2.UndirectedGraph import UndirectedGraph
from projecto_discretas_2.DirectedGraph import DirectedGraph
from projecto_discretas_2.graph_loader import load_graph_from_file
from projecto_discretas_2.algorithms import is_connected, has_cycle, is_tree, is_forest
from projecto_discretas_2.graph_loader import load_graph_from_file


def main():
    graph = UndirectedGraph()
    load_graph_from_file(graph, "data/ejemplo_3.csv")

    is_connected(graph)
    has_cycle(graph)
    is_tree(graph)
    is_forest(graph)

if __name__ == "__main__":
    main()

