from collections import namedtuple
Graph = namedtuple('Graph', ["vertices", "edges"])
edges = [(0, 1,3), (0, 3,2), (0, 2,4), (1, 2,1)]
vertices = [0, 1, 2, 3]
G = Graph(vertices, edges)
def adjacent_dict(Graph):
    adj = {node: [] for node in Graph.vertices}
    for edge in G.edges:
        node1, node2 = edge[0], edge[1]
        adj[node1].append(node2)
        adj[node2].append(node1)
    print(adj)
    return adj

def adjacent_matrix(Graph):
    A = [[0 for i in Graph.vertices] for j in Graph.vertices]
    for edge in Graph.edges:
        node1, node2 = edge[0], edge[1]
        A[node1][node2] = 1
        A[node2][node1] = 1
    print(A)

def adjacent_matrix_weight(Graph):
    A = [[0 for i in Graph.vertices] for j in Graph.vertices]
    for edge in Graph.edges:
        node1, node2, weight = edge[0], edge[1], edge[2]
        A[node1][node2] = weight
        A[node2][node1] = weight
    print(A)

adjacent_dict(G)
adjacent_matrix(G)
adjacent_matrix_weight(G)