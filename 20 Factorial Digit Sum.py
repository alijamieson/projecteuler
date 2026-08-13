# n! means n * (n-1) * ... * 3 * 2 * 1.
# For example, 10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 3628800.
# The sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!
import math

n = math.factorial(100)
sum = 0

while n > 0:
    sum += n % 10  # extract last digit
    n //= 10       # remove last digit

print(sum)