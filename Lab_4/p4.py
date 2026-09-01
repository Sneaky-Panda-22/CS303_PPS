with open("Rolls.csv","r") as file:
    user_dict = {line.split(',')[0][1:-1]:line.split(',')[1].split()[0][1:] for line in file}

for key,val in user_dict.items():
    print(f"{key} : {val}")