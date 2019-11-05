from graph import Graph
from util import Stack


class AncestorGraph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            # self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)

    # def print_verts(self):
    #     print(self.vertices)


def earliest_ancestor(ancestors, starting_node):
    """
    Write a function that, given the dataset and the ID of an individual in the dataset, 
    returns their earliest known ancestor – the one at the farthest distance from the input individual.
    If there is more than one ancestor tied for "earliest", 
    return the one with the lowest numeric ID. If the input individual has no parents, the function should return -1.
    25 lines

    """
    # build the goddamn graph
    # ancestors is a list of pairs, we need to loop through it and find our verts and edges
    vert_list = []
    for ancestor in ancestors:
        # print(ancestor)
        vert_list.append(ancestor[0])
        vert_list.append(ancestor[1])
        # vert_list.sort()
    # print(vert_list)
    # create verts for each unique value in vert_list
    graph = AncestorGraph()
    for v in vert_list:
        graph.add_vertex(v)
    # graph.print_verts()
    # need to add edges
    for ancestor in ancestors:
        graph.add_edge(ancestor[0], ancestor[1])
    # graph built! now traverse and find the furthest ancestor away from starting_node
    # Going to use a Depth First Traversal
    # Create an empty stack, push starting node to stack
    s = Stack()
    s.push(starting_node)
    # Create a Set to store visited vertices
    visited = set()
    # list to hold found ancestors
    ancestor_list = []
    # While the stack is not empty...
    while s.size() > 0:
        # Pop the first vertex
        v = s.pop()
        # If that vertex has not been visited...
        if v not in visited:
            # Mark it as visited...
            visited.add(v)
            # Then add all of its neighbors to the top of the stack
            for neighbor in graph.vertices[v]:
                # print(neighbor, 'neigh')
                # append the nighbors to ancestor list. This works such that when it finishes the DFT,
                # the furthest neighbor(ancestor) away is at the end of the list.
                ancestor_list.append(neighbor)
                # push neighbor to keep traversing
                s.push(neighbor)
    # print(ancestor_list, 'ans list')
    # if the ancestor list is empty, then there are no parents. return -1
    if len(ancestor_list) == 0:
        answer = -1
    # else, there are parents, and we want the last one, which is also the furthest away
    else:
        answer = ancestor_list[-1]

    # print(answer)
    return answer


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

# earliest_ancestor(test_ancestors, 4)


"""

  s = Stack()
    s.push([starting_node])
    # Create a Set to store visited vertices
    visited = set()
    ancestor_list = []
    # While the stack is not empty...
    while s.size() > 0:
            # Pop the first vertex
        v = s.pop()
        # If that vertex has not been visited...
        if v not in visited:
            # Mark it as visited...
            # print(v, 'non recur print')
            ancestor_list.append(v)
            visited.add(v)
            # Then add all of its neighbors to the top of the stack
            # print(graph.vertices[v], 'graph.verts')
            for neighbor in graph.vertices[v]:
                s.push(neighbor)
    answer = ancestor_list[-1]
    print(ancestor_list)
    if len(ancestor_list) == 1:
        answer = -1

    print(answer)
    return answer


"""
