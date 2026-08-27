# The decimal number 585 = 1001001001 in binary is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2
# (Please note that the palindromic number, in either base, may not include leading zeros.)
# https://www.w3schools.com/python/ref_func_bin.asp
# https://www.w3schools.com/python/python_howto_reverse_string.asp

def basetwo():
    c=0
    for i in range(0,1000000):
        j = bin(i)[2:]
        if j==j[::-1] and str(i)==str(i)[::-1]:
            c+=i
    return(c)
print(basetwo())