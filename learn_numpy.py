import numpy as np
import numpy.linalg as LA

def gs_cofficient(a, b):
    denominator = np.dot(b, b)
    if denominator == 0:
        return 0
    return np.dot(a, b) / np.dot(b, b) # getting the coefficient for each b_i

def gs_process(A):
    B = []
    for i in np.arange(A.shape[0]):
        a_i = A[i]
        for b in B :
            proj_vec = gs_cofficient(a_i, b) * b
            a_i = a_i - proj_vec
        B.append(a_i)
    return np.array(B)



# to normalize the basis:
def normalize(X):
    return np.array([x / LA.norm(x)
                     if LA.norm(x) != 0
                     else np.zeros(len(x))
                     for x in X])


A = np.array([[3, 1, -2],
              [1, 1, 1],
              [-1, 2, 4]])
q, r = LA.qr(A)
#print(q@r)
#print("Q=", q)
#print("R=", r)
#print('sum', sum([sum(r[i]) for i in range(len(r))]))
is_equal = np.allclose(A, np.dot(q,r))
#print("Obtained the original matrix?", is_equal)
#if you need to force negative/positive diagonal values
for i in range(1, len(A)):
    for j in range(len(A)):
        q[j][i] *= -1
        r[i][j] *= -1
#print("Q=", q)
#print("R=", r)
is_equal = np.allclose(A, np.dot(q,r))
#print("Obtained the original matrix?", is_equal)
#print(sum([sum(r[i]) for i in range(len(r))]))
#print(q@r)

#example use
a1 = np.array([12, 10, 2, 0])
a2 = np.array([5, 8, 0, 1])
a3 = np.array([1, 0, 1, -1])
A = np.array([a1, a2, a3])
basis = gs_process(A)
print("Orthogonal basis:\n", basis)
print(LA.norm(basis[2]))
normalized = normalize(basis)
#print("Orthonormal basis:\n", normalized)