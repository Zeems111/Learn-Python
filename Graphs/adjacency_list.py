def edgesCount(adj_list):
    n = len(adj_list)
    edges_count = 0

    for i, adj_vertex in enumerate(adj_list):
        for k in adj_vertex:
            if k > i:
                edges_count += 1

    return edges_count

def reverseGraph(adj_list):
    n = len(adj_list)
    reversed_graph = [[] for i in range(n)]
    for i in range(n):
        for k in adj_list[i]:
            reversed_graph[k].append(i)
    return reversed_graph

def isTransitive(adj_list):
    n = len(adj_list)
    is_transitive = True
    for v1 in range(n):
        for v2 in adj_list[v1]:
            for v3 in adj_list[v2]:
                if v3 not in adj_list[v1]:
                    is_transitive = False
    # YOUR CODE GOES HERE

    return is_transitive


adj_list = [[], [], [], [], []]
print(isTransitive(adj_list))