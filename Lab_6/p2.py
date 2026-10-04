import numpy as np  

M = np.array([[1,2,3],[2,4,5],[3,5,6]])
b = np.array([[1],[2],[3]])

M_INV = np.linalg.inv(M)
#print(M_INV) 
# allclose is used to check floating point nos.
#print(np.allclose(M.dot(M_INV),np.eye(3)))
x,y,z = M_INV.dot(b)
print(f"Using .dot()\nx = {x}\ny = {y}\nz = {z}")
print(f"\nUsing np.linalg.solve()\n{np.linalg.solve(M,b)}\n")
# print(np.allclose(M_INV.dot(b),np.linalg.solve(M,b))) True

u = M.reshape(-1)
print("Norm calculated:",np.sqrt(u.dot(u))) #11.357816691600547
print("Norm using np.linalg.norm:",np.linalg.norm(M)) #11.357816691600547

eigenvalue,eigenvector = np.linalg.eig(M)
print("\nEigen Values:\n",eigenvalue)
print("Eigen Vector:\n",eigenvector)
print("")
# checking Mv = λv for all. outputs true!
# print(np.allclose(M.dot(eigenvector[:,0]),eigenvalue[0]*eigenvector[:,0]))
# print(np.allclose(M.dot(eigenvector[:,1]),eigenvalue[1]*eigenvector[:,1]))
# print(np.allclose(M.dot(eigenvector[:,2]),eigenvalue[2]*eigenvector[:,2]))

det_M = np.linalg.det(M)
print("Determinant of M:",det_M)
print("Product of eigenvalues:",np.prod(eigenvalue))

# print(np.allclose(det_M,np.prod(eigenvalue))) true!