n = int(input("enter n: "))
a,b = 0,1

for i in range(n):
    print(f"{b}", end = " ")
    a,b = b,a+b
print("")