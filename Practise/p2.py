file_name = "population.txt"
file = open(file_name, "r")

population = {}

for line in file:
    parts = line.split();
    state = parts[0]
    city = parts[1]
    people = parts[2].replace(",","")

    if state in population.keys():
        population[state][city] = people
    else:
        population.