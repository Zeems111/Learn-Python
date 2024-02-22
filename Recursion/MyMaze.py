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

def can_reach(maze, i=0, j=0):
    m = len(maze)
    n = len(maze[0])
    if (i, j) == (m-1, n-1):
        return True

    for (x, y) in [(i, j+1), (i+1, j), (i-1, j), (i, j-1)]:
        if 0 <= x < m and 0 <= y < n and maze[x][y] == 0:
            maze[i][j] = 1
            reachable = can_reach(maze, x, y)
            maze[i][j] = 0
            return reachable
    return False


def all_paths(maze, i=0, j=0):
    m = len(maze)
    n = len(maze[0])
    path = []
    if (i, j) == (m-1, n-1):
        path = [(i, j)]
        return path
    else:

        for x, y in [(i, j+1), (i+1, j), (i-1, j), (i, j-1)]:
            if 0 <= x < m and 0 <= y < n and maze[x][y] == 0:
                maze[i][j] = 1
                path = [(i, j)] + all_paths(maze, x, y)
                maze[i][j] = 0
                return path
        return []


if __name__ == '__main__':
    maze = [[0, 1, 0],
            [0, 1, 0],
            [0, 0, 0]]

    reachable = can_reach(maze)
    paths = all_paths(maze)
    print(reachable)
    print(paths)
