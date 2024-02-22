from itertools import product

n = 5
#Omega = set(product(['H', 'T'], repeat=n))
Omega = set(product([*range(1, 7)], repeat=n))
def prob(X):
    return len(X)/len(Omega)

def conditional_prob(X, given):
    if not X or not given:
        return 0
    return len(X & given)/len(given)

def are_independent(X, Y):
    return prob(X & Y) == prob(X) * prob(Y)

def prod(X):
    res = 1
    for x in X:
        res *= x
    return res

A = set(om for om in Omega if sum(om) % 3 == 0)
B = set(om for om in Omega if prod(om) > 500)
print('A:', *A, sep='\n')
print('B:', *B, sep='\n')
print('P(B|A) =', conditional_prob(B, given=A))
'''
print(*Omega, sep='\n')
A = set(om for om in Omega if om.count('H') % 2 == 0)
B = set(om for om in Omega if om.count('T') < 4)
print('A:', *A, sep='\n')
print('B:', *B, sep='\n')
print(len(Omega), len(A), len(B))
print(conditional_prob(A, given=B))
'''


