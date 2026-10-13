import numpy as np 
rng = np.random.default_rng(seed = 303)
N = 1000
# for 1D points
print("Points from 1d unit line:")
points = rng.uniform(0.0,1.0,size=(N,))
X = points.reshape(1,-1)
Y = points.reshape(-1,1)
dist_matrix_1D = abs(X-Y)
# print(dist_matrix_1D)
print(f"Shape of Distance matrix: {dist_matrix_1D.shape}")
# for 2D points
print("\nPoints from 2d unit square:")
points = rng.uniform(0.0,1.0,size=(N,2))
X = points.reshape(1,N,2)
Y = points.reshape(N,1,2)
dist_matrix_2D = ((abs(X-Y)**2).sum(axis=2))**0.5
# print(dist_matrix_2D)
print(f"Shape of Distance matrix is: {dist_matrix_2D.shape}\n")

#N(0,1)
print("Points from standard normal:")
points = rng.standard_normal(size=(N,))
X = points.reshape(1,-1)
Y = points.reshape(-1,1)
dist_matrix_1D = abs(X-Y)
# print(dist_matrix_1D)
print(f"Shape of Distance matrix: {dist_matrix_1D.shape}")

