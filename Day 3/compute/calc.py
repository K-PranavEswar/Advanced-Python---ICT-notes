def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y
def modulus(x, y):
    if y == 0:
        return "Error: Modulus by zero is not allowed."
    return x % y
def exponentiate(x, y):
    return x ** y
def floor_divide(x, y):
    if y == 0:
        return "Error: Floor division by zero is not allowed."
    return x // y