class DirectedGraph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex): #Añadir vértices
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = {}

    def add_edge(self, source, target, weight=1): #Añadir aristas
        self.add_vertex(source)
        self.add_vertex(target)
        self.adjacency_list[source][target] = weight

    def get_neighbors(self, vertex): #Consultar vecinos
        return self.adjacency_list.get(vertex, {})
