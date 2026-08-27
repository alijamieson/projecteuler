# What is the largest prime factor of the number 600851475143?

n = 600851475143

import math 
def prime_factors(num):
  factors = []
  factor = 2

  while (num >= 2):
    if (num % factor == 0):
      factors.append(factor)
      num = num / factor
    else:
      factor += 1
  return factors

print(max(prime_factors(n)))