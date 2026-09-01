marks = [35,78,92,21,55,40]
res = ["Fail" if x < 30 else "Distinction" if x > 80 else "Pass" for x in marks]
print(res)