# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million

def is_prime(n):
	if n < 2:
		return False

	i = 2
    while i * i <= n:
		if n % i == 0:
			return False
		i += 1

	return True
i=0
d=0
while True:

print(d)
