import numpy as np  

def numpy_prod(a,b):
    ans = a.dot(b)
    return ans

def normal_prod(a,b):
    ans = sum((x*y for (x,y) in zip(a,b)))
    return ans

#0.04s user 0.01s system 93% cpu 0.058 total
u = np.array([1,2,3])
v = np.array([10,20,30])
ans = numpy_prod(u,v)
print(ans)

#0.05s user 0.01s system 95% cpu 0.061 total
a = [1,2,3]
b = [10,20,30]
ans = normal_prod(a,b)
print(ans) 