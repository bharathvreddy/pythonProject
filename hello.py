def greet(name, age, is_male, is_tall):
    print("Hi "+ name +", Good Morning !, You are "+str(age)+" old.")
    if is_male and is_tall:
        print("You are tall and male")
    elif is_male:
        print("You are male but not tall.")
    elif is_tall:
        print("You are tall but not male")
    else:
        print("You are neither male nor tall.")

greet("Bharath", 29, True, True)