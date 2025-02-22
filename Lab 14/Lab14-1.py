import numpy as np

a = np.array([1, 2, 3,
              4, 5, 6,
              7, 8, 9])

b = np.array([9, 8, 7,
              6, 5, 4,
              3, 2, 1])

A = a.reshape(3,3)
B = b.reshape(3,3)

print(A)
print(B)
print((A**2) + (2*B))
print(((A+B).T) * (A - B))