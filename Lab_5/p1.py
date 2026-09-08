U = [1,2,3,4]
V = [10,20,30,40]

ans = int(sum(x*y for x,y in zip(U,V)))

print(ans)