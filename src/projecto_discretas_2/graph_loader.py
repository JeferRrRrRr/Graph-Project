def load_graph_from_file(graph, file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            clean_line = line.strip()
            if not clean_line or clean_line.lower().startswith("source,"):
                continue
            source, target, weight = clean_line.split(",")
            graph.add_edge(source.strip(), target.strip(), int(weight.strip()))
    return graph