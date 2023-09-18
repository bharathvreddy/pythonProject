def pow(base, power):
    result = 1
    for index in range(power):
        result *= base
    return result


print(pow(5, 2) == 2**5)