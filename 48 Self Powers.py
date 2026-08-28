# The series 1^1 + 2^2 + 3^3 + ... 10^10 = 10405071317
# Find the last 10 digits of the series 1^1 + 2^2 + 3^3 + ... 1000^1000.
a=-1
for i in range(1001):
    a+=i**i

n = 10

ch = str(a)[-n:]
print(ch)