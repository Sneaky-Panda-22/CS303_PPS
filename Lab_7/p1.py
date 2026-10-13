import numpy as np
rng = np.random.default_rng(seed = 303)
A = rng.random((5,5))
column_mean = np.mean(A,axis=0)
ans = A - column_mean
print(ans)