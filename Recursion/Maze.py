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

import copy
import math


def weighted_escapes(maze, w):
    def weighted_len(path):
        return sum(map(lambda x: x[1], path))


    def can_escape(maze, path, best, w, i=0, j=0):
        count = 0
        # (i, j) is the starting position
        # maze[x][y] = 0 <=> (x, y) cell is empty
        # maze[x][y] = 1 <=> (x, y) cell contains a wall
        n = len(maze)
        m = len(maze[0])

        if i == n - 1 and j == m - 1:
            path.append(((i, j), 1))
            best.append(copy.deepcopy(path))
            path.pop()
            return 1

        state = maze[i][j]
        maze[i][j] = -1
        path.append(((i, j), (w-1) * (state) + 1))

        result = math.inf

        for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
            if 0 <= a < n and 0 <= b < m and maze[a][b] in [0, 1]:
                result = min(result, can_escape(maze, path, best, w, a, b))

        maze[i][j] = state
        path.pop()
        return result

    path = []
    best = []
    can_escape(maze, path, best, w)

    min_len_path = min(best, key=weighted_len)
    min_len = weighted_len(min_len_path)
    best = list(filter(lambda x: weighted_len(x) == min_len, best))

    best = list(map(lambda path: list(map(lambda x: x[0], path)), best))
    best = list(map(sorted, best))
    return sorted(best)

maze = [
      [0, 1, 0],
      [0, 0, 0],
      [1, 1, 0]

    ]
"""
maze = [
      [0, 1, 1, 1, 1],
      [0, 1, 0, 1, 0],
      [0, 0, 1, 1, 0],
      [0, 0, 0, 0, 0]
    ]
"""
bst = weighted_escapes(maze, 0)
print(*bst, sep='\n')
