def add_one(number):
    return number + 1


def add_two(number):
    return number + 2


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b
