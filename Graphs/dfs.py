def sameComponent(adj_matrix, vertex):
    graph = adj_matrix
    n = len(graph)
    visited = [False for i in range(n)]
    vertex_count = []

    def dfs(v):
        vertex_count.append(v)
        visited[v] = True
        for i in range(len(graph)):
            if graph[v][i] == 1 and (not visited[i]):
                #print('v:', v, 'i:', i)
                dfs(i)

    dfs(vertex)
    return len(vertex_count)


adj_matrix = [[0, 1, 1, 0, 0, ],
              [1, 0, 1, 0, 0, ],
              [1, 1, 0, 0, 0, ],
              [0, 0, 0, 0, 0, ],
              [0, 0, 0, 0, 0, ],]
vertex = 0
print(sameComponent(adj_matrix, vertex))

adj_matrix = [[0, 1, 0, 0, 0, 0, 0, 0, ],
              [1, 0, 1, 0, 0, 0, 0, 0, ],
              [0, 1, 0, 1, 0, 0, 0, 0, ],
              [0, 0, 1, 0, 0, 0, 0, 0, ],
              [0, 0, 0, 0, 0, 1, 0, 0, ],
              [0, 0, 0, 0, 1, 0, 1, 0, ],
              [0, 0, 0, 0, 0, 1, 0, 1, ],
              [0, 0, 0, 0, 0, 0, 1, 0, ],]
vertex = 0
print(sameComponent(adj_matrix, vertex))