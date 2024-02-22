"""
A maze defined by a 2-d array maze where maze[i][j] is equal to 0
if the j-th cell on the i-th row is empty and 1 if there is a wall there.
It is guaranteed that the upper left and lower right cells are empty.
A path can go from a cell to a cell that shares a side with it.

Output:
Returns True if there exists a path from the upper left cell to the lower right
cell passing through empty cells only.
Returns False otherwise.


"""



# 2
def ks_fastest_escapes(maze):
    def __fastest_escapes(i=0, j=0, path=None):
        if path is None:
            path = [(i, j)]

        if i == N - 1 and j == M - 1:
            yield path
        else:
            maze[i][j] = 1
            for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                if (
                    0 <= a < N
                    and 0 <= b < M
                    and not maze[a][b]
                ):
                    yield from __fastest_escapes(a, b, path + [(a, b)])
            maze[i][j] = 0

    def path_len(path):
        if path is not None:
            return len(path)

    N = len(maze)
    M = len(maze[0])
    if maze[0][0] == 1:
        return []

    paths = list(__fastest_escapes())
    lens = list(map(path_len, paths))
    if lens:
        paths = [sorted(path) for path in paths if len(path) == min(lens)]

    return list(sorted(paths))





maze = [
      [0, 0, 1],
      [0, 1, 0],
      [1, 0, 0]

    ]
""" 
maze = [
      [0, 1, 1, 1, 1],
      [0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0],
      [0, 0, 1, 0, 0]
    ]

maze = [
      [0, 0, 0, 1, 0, 0, 0],
      [0, 1, 0, 0, 0, 1, 0],
      [0, 1, 1, 1, 0, 0, 0],
      [0, 0, 0, 1, 0, 1, 0]
    ]
    """
for _ in range(10000):
    m = random.randint(2,10)
    n = random.randint(2,10)
    maze = [[random.randint(0, 1) for j in range(m)] for i in range(n)]

    bst1 = my_fastest_escapes(maze)
    #print(bst1, sep='\n')
    #print()
    bst2 = ks_fastest_escapes(maze)
    #print(bst2, sep='\n')
    if bst1 != bst2:
        print('maze', *maze)
        print()
        print('Кс', bst2, sep="\n")
        print()
        print('Моё', bst1, sep="\n")

print('ok!')