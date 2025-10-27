# Program to perform basic arithmetic operations

# Take input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Addition
sum_result = num1 + num2
print("Addition:", num1, "+", num2, "=", sum_result)

# Subtraction
difference = num1 - num2
print("Subtraction:", num1, "-", num2, "=", difference)

# Multiplication
product = num1 * num2
print("Multiplication:", num1, "*", num2, "=", product)

# Division (check for division by zero)
if num2 != 0:
    quotient = num1 / num2
    print("Division:", num1, "/", num2, "=", quotient)
else:
    print("Division: Error! Division by zero is not allowed.")

# Modulus (check for division by zero)
if num2 != 0:
    remainder = num1 % num2
    print("Modulus:", num1, "%", num2, "=", remainder)
else:
    print("Modulus: Error! Division by zero is not allowed.")
