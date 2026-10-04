import numpy as np 

f = lambda x: np.exp(-x**2)

n = int(1e6)
a, b = 0, 1

def RR(f, a, b, n):
    dx = (b - a) / n
    temp = np.arange(1, n + 1) * dx + a
    return np.sum(f(temp)) * dx

def LR(f, a, b, n):
    dx = (b - a) / n
    temp = np.arange(0, n) * dx + a
    return np.sum(f(temp)) * dx

left_sum, right_sum = LR(f, a, b, n), RR(f, a, b, n)
print("Left Riemann Sum:", left_sum)
print("Right Riemann Sum:", right_sum)
print("Difference between Right and Left Sum:", abs(right_sum - left_sum))

# using 10^6 intervals, the error is 10^-7
# to find the value of n for which the error is 10-6, we can use z distribution,
# x^2 = (z^2)/2 => z = x*sqrt(2)
#the actual value of intergrand is Z(1.41) - Z(0) = 0.92135 - 0.5 = 0.42135
# emperical error in left reimann sum is given as: ((b-a)/2*n)*abs(f(b)-f(a)) 
#10^-6 = (1/2*n)*abs(1/e-1) => n = 316060.28 
#if we choose n = 316061 the error will match!

n1, n2 = 316060, 316061

# we can also take average to get high precision value of actual integrand value
calculated_val = (left_sum + right_sum) / 2

error_std1 = abs(calculated_val - LR(f, a, b, n1))
error_std2 = abs(calculated_val - LR(f, a, b, n2))

print(f"Error in 316060: {error_std1}")
print(f"Error in 316061: {error_std2}")



#---------------------------------------------------
# other method by LLM: using scipy are erf

# import numpy as np 
# from scipy.special import erf  # Provides the exact analytical value of the error function

# f = lambda x: np.exp(-x**2)
# a, b = 0, 1

# def RR(f, a, b, n):
#     dx = (b - a) / n
#     temp = np.arange(1, n + 1) * dx + a
#     return np.sum(f(temp)) * dx

# def LR(f, a, b, n):
#     dx = (b - a) / n
#     temp = np.arange(0, n) * dx + a
#     return np.sum(f(temp)) * dx

# left_sum, right_sum = LR(f, a, b, int(1e6)), RR(f, a, b, int(1e6))
# print("Left Riemann Sum:", left_sum)
# print("Right Riemann Sum:", right_sum)
# print("Difference between Right and Left Sum:", abs(right_sum - left_sum))

# # The true analytical value of the integral from 0 to 1 is exactly (sqrt(pi)/2) * erf(1)
# # Written out in full precision: 0.7468241328124271
# calculated_val = (np.sqrt(np.pi) / 2) * erf(1)

# n1, n2 = 316060, 316061

# error_std1 = abs(calculated_val - LR(f, a, b, n1))
# error_std2 = abs(calculated_val - LR(f, a, b, n2))

# print(f"Error in 316060: {error_std1:.12e}  (Greater than 10^-6)")
# print(f"Error in 316061: {error_std2:.12e}  (Less than 10^-6 !)")
