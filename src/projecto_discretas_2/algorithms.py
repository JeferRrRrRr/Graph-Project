def is_connected(graph):
    vertices = list(graph.adjacency_list.keys())

    if len(vertices) == 0:
        print("is_connected: True")
        return True

    start_vertex = vertices[0]
    visited = {start_vertex}
    queue = [start_vertex]

    while len(queue) > 0:
        current = queue.pop(0)
        for neighbor in graph.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    result = len(visited) == len(vertices)
    print(f"is_connected: {result}")
    return result

def has_cycle(graph):
    visited = set()

    for vertex in graph.adjacency_list:
        if vertex not in visited:
            visited.add(vertex)
            queue = [(vertex, None)]

            while len(queue) > 0:
                current, parent = queue.pop(0)

                for neighbor in graph.get_neighbors(current):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, current))
                    elif neighbor != parent:
                        print("has_cycle: True")
                        return True

    print("has_cycle: False")
    return False

def is_tree(graph):
    if len(graph.adjacency_list) == 0:
        print("is_tree: False")
        return False

    connected = is_connected(graph)
    cycle = has_cycle(graph)

    result = connected and not cycle
    print(f"is_tree: {result}")
    return result

def is_forest(graph):
    if len(graph.adjacency_list) == 0:
        print("is_forest: False")
        return False

    cycle = has_cycle(graph)

    result = not cycle
    print(f"is_forest: {result}")
    return result