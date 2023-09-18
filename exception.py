# from math import factorial

try:
    dividend = int(input("Enter a dividend: "))
    divisor = int(input("Enter a divisor: "))

    print("Quotient = " + str((dividend // divisor)) +" Reminder = "+ str(dividend % divisor))
except ZeroDivisionError as err:
    print("Dude something went wrong!!! "+ err)