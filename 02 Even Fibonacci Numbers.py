# for Fibonacci numbers below 4 million, find the sum of even valued terms

f1=1
f2=1
n=0
for i in range(4000000):
    f3=f1+f2
    if f3>=4000000:
        break
    f1=f2
    f2=f3
    #print(f3)
    if f3 % 2==0:
        n+=f3
print(n)