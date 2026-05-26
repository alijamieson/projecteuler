# The sum of the squares of the first ten natural numbers is 1^2 + 2^2 + ... 10^2 = 385.

# The square of the sum of the first ten natural numbers is (1 + 2 + ... 10)^2 = 3025.

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

target = 100

def sumofsq():
    global a
    a=0
    for i in range(target+1):
        a+=(i**2)
    # print(a)


def sqofsum():
    global d
    d=0
    for j in range(target+1):
        d+=j
    # print(d**2)

sqofsum()
sumofsq()

print((d**2)-a)

