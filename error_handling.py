import sys

print("Enter two numbers.....\n")


n1 = int(input("n1: "))
n2 = int(input("n2: "))


try:
    result = n1 / n2
except ZeroDivisionError:
    print("\nCannot divide a number by zero")
    sys.exit(1)


print(f"\nThe result of {n1}/{n2} is {result}")
