A = {'a':1,'b':2,'c':1}
new_dict = {val:{key for key,value in A.items() if val==value} for keys,val in A.items()}
print(new_dict)
