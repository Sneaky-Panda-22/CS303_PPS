import numpy as np 
a = np.arange(0,32,2).reshape(4,4)
print(a)
diag = np.diag(a)
temp = np.fliplr(a)
anti_diag = np.diag(temp)
print(diag,anti_diag)