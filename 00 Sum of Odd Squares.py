# sum the square numbers of odd integers below 839000

n = 0

for i in range(1, 839000, 2):
    n+=i**2

print(n)