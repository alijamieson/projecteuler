# what is the 10001st prime number?

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
n=0
while True:
	if n==10001:
		break
	if is_prime(i):
		n+=1

	#print(i,"is",n)
	i+=1
print(i-1)
