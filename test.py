import math


def increase(n):
    if n == 10:
        return n
    else:
        x = 1+increase(n+1);
        print("n = ", n , "result = ",x)
        return x
print(increase(1))

from math import *
print(math.factorial(20))