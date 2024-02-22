def isTree(adj_list):
    graph = adj_list
    n = len(graph)
    visited = [False for i in range(n)]
    vertex_count = []
    def dfs(v):
        is_tree = True
        vertex_count.append(v)
        visited[v] = True
        for i in graph[v]:
            if visited[i] and vertex_count[-2] != i:
                #print(vertex_count)
                #print("v:", v, "i:", i)
                is_tree = False
            elif not visited[i]:
                #print('v:', v, 'i:', i)
                dfs(i)
        #print(vertex_count)
        return is_tree and len(vertex_count) == n

    return dfs(0)


adj_list = [[1], [0, 2], [1, 3], [2, 4], [3, 5], [4], []]
print(isTree(adj_list))

adj_list = [[1], [0, 2], [1]]
print(isTree(adj_list))