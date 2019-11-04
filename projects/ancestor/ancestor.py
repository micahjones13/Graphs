from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    pass


graph = Graph()
# add the verts
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)
graph.add_vertex(6)
graph.add_vertex(7)
graph.add_vertex(8)
graph.add_vertex(9)
graph.add_vertex(10)
graph.add_vertex(11)
# add edges
graph.add_edge(1, 3)
graph.add_edge(2, 3)
graph.add_edge(3, 6)
graph.add_edge(5, 6)
graph.add_edge(5, 7)
graph.add_edge(4, 5)
graph.add_edge(4, 8)
graph.add_edge(8, 9)
graph.add_edge(11, 8)
graph.add_edge(10, 1)
