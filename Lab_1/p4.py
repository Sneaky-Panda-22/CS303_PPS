n = int(input("Enter n: "))
sum, squared_sum = 0, 0

print(f"Enter {n} numbers: ")

for i in range(n):
    x = int(input())
    sum = sum + x
    squared_sum = squared_sum + x**2

mean = sum/n
standard_deviation = (squared_sum/n - mean**2)**0.5
variance = squared_sum/n - mean**2
print(f"standard deviation: {standard_deviation}\nVariance: {variance}")