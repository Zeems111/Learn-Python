import numpy as np
C = np.array([[1, 2, 3, -1]])
B = np.array([[1, 3, 1, 0],
              [1, 0, -1, 2],
              [0, 0, 1, 2],
              [-1, 1, 0, 1]
              ])
print(C.T@C@B.T@B)

A = np.array([[1, 1, 2, -1],
              [-1, 0, 3, 2],
              [2, -1, 1, 0],
              [0, 1, 5, 1]
              ])
print(np.linalg.matrix_rank(A))