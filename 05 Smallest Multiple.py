# 2520  is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
j=2520
a=False
while not a:
    print(j)
    print("      ")
    b=[]
    a=True
    for i in range(1,20):
        if j % i != 0:
            a=False
            break
    j+=j
print(j)