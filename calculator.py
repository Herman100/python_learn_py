n1 = float(input("Enter first number: ").strip())

n2 = float(input("\n\nEnter second number: ").strip())


def add(n1, n2):

    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        return "Cannot divide by zero"
    return n1 / n2


def power(n1, n2):
    return n1**n2


def floor_divide(n1, n2):
    if n2 == 0:
        return "Cannot divide by zero"
    return n1 // n2


def modulus(n1, n2):
    return n1 % n2


opt = input("\n\nEnter an operation (+, -, *, /, **, //, %): ").strip()


def calculator(n, n2, opt):
    if opt == "+":
        return add(n, n2)
    elif opt == "-":
        return subtract(n, n2)
    elif opt == "*":
        return multiply(n, n2)
    elif opt == "/":
        return divide(n, n2)
    elif opt == "**":
        return power(n, n2)
    elif opt == "//":
        return floor_divide(n, n2)
    elif opt == "%":
        return modulus(n, n2)
    else:
        return "Invalid operation"


result = calculator(n1, n2, opt)
print(
    "\n",
    (
        result
        if isinstance(result, str)
        else f"The result of {n1} {opt} {n2} is: {result}"
    ),
)
