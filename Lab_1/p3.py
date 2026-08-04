n = int(input("Enter n: "))
sum, max_el, min_el = 0, float('-inf'), float('inf')

print(f"Enter {n} numbers: ")

for i in range(n):
    x = int(input())
    sum = sum + x

    if x > max_el:
        max_el = x
    elif x < min_el:
        min_el = x

mean = sum/n

print(f"Mean: {mean}\n Maximum Element: {max_el}\n Minimum Element: {min_el}")