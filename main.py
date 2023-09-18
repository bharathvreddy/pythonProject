'''def fact(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n*fact(n-1)


print(fact(5))'''

def dectobin(n):
    assert int(n)==n,'Enter only decimal number'
    if n==0:
        return 0
    else:

        x=n%2+10*dectobin(int(n/2))
        print('n=',n ,'result=',x)
        return x

print(dectobin(12))

