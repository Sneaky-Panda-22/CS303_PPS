n = int(input("Enter number: "))

def is_prime(n): return all(n%i !=0 for i in range(2,1+int(n**0.5)))
print(is_prime(n))