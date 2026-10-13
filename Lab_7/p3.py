import numpy as np 
rng = np.random.default_rng(seed = 303)
A = rng.integers(-100,101,size = (50,))
A[A<0] = 0
B = A - 50
min_dist  = np.argmin(abs(B))
print(A[min_dist])