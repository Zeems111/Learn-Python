def hasLoops(adj_matrix):
    n = len(adj_matrix)
    has_loops = False
    for i in range(n):
        if adj_matrix[i][i] == 1:
            has_loops = True
            break
    return has_loops

def isUndirected(adj_matrix):
    n = len(adj_matrix)
    is_undirected = True
    for i in range(n):
        if adj_matrix[i][i] == 1:
            is_undirected = False

        for j in range(n):
            if adj_matrix[i][j] != adj_matrix[j][i]:
                is_undirected = False
            break
    return is_undirected

def countEdges(adj_matrix):
    n = len(adj_matrix)
    edges_count = 0

    for i in range(n):
        for j in range(i, n):
            edges_count += adj_matrix[i][j]
    return edges_count

adj_matrix = [[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, ],
[0, 0, 0, 1, 1, 1, 1, 1, 1, 1, ],
[1, 0, 0, 1, 1, 1, 1, 1, 0, 0, ],
[1, 1, 1, 0, 1, 0, 1, 1, 1, 1, ],
[1, 1, 1, 1, 0, 1, 1, 1, 1, 1, ],
[1, 1, 1, 0, 1, 0, 0, 1, 1, 1, ],
[1, 1, 1, 1, 1, 0, 0, 1, 0, 1, ],
[1, 1, 1, 1, 1, 1, 1, 0, 1, 0, ],
[1, 1, 0, 1, 1, 1, 0, 1, 0, 0, ],
[1, 1, 0, 1, 1, 1, 1, 0, 0, 0, ], ]
print(countEdges(adj_matrix))