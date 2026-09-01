import numpy as np
linkedin_connections = np.array([
    [0,0,1,0,0],
    [0,1,1,1,0],
    [1,0,1,1,1],
    [0,0,0,0,0],
    [0,1,0,1,0]
])

temp = linkedin_connections @ linkedin_connections
#print(temp)

res = {i+1:[j+1 for j in range(len(temp)) if temp[i][j] > 0 and i!=j and linkedin_connections[i][j]==0 ]for i in range(len(temp))}

print(res)