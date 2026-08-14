# 2520  is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

for j in range(1,10000000000000000000000):
    b=[]
    a=True
    for i in range(1,20):
        if j % i != 0:
            a=False
            break
    if a:
        break
print(j)