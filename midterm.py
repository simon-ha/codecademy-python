# Codecademy Practice Makes Perfect

# create a function that determines if x is an even number
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

print is_even(45)

# fxn to see if x is an int
def is_int(x):
    if x - round(x) != 0:
        return False
    else:
        return True

# summing the digits of a number
def digit_sum(n):
    substring = str(n)
    y = 0
    for x in substring:
        y = int(x) + y
    return y

print digit_sum(1234567)

# factorial of a number
def factorial(x):
    y = 1
    if x < 0:
        print "cannot factorial a negative"
    elif x == 0:
        return 1
    else:
        for i in range(1, x+1):
            y = y * i
    return y

print factorial(10)
