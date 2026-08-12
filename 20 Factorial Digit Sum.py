# n! means n * (n-1) * ... * 3 * 2 * 1.
# For example, 10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 3628800.
# The sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!
import math

n=0

# a=str(math.factorial(10))
a = 10
for i in range(1, a):
    n+=i
print(n)
dict(c=None)