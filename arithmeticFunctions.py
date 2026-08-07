# plus one
def plus_one (number):
    return number + 1


# add numbers
def add (number1, number2): 
    result = 0
    # checking the greater number to avoid stressing the computer's memory too much
    # E.g The sum operation between 5 and 85 is better if the computer adds 1 to 85 five times than to add 1 to 5 eighty five times.
    if number1 > number2:
        result = number1 # starting at the larger number
        for i in range(number2):
            result = plus_one(result) # adding one to the previous value
            
    else: 
        result = number2 # starting at the larger number
        for i in range(number1):
            result = plus_one(result) # adding one to the previous value

    return result


print(add(2, 1))
print(add(5, 85))
print(add(85, 5))
print(add(3, 4))

# number doubler
def number_doubler (number):
    return number + number

# multiply 
def multiply (number1, number2):
    result = 0
    # using the same logic of finding out the larger number
    if number1 > number2:
        result = number1
        for i in range(number2):
            result = number_doubler(result)
    else:
        result = number2
        for i in range(number1):
            result = number_doubler(result)


    return result

print(multiply(2, 3))