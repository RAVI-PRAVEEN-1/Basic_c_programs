# Program to find the modulus of two numbers

# Take input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Check for division by zero
if num2 != 0:
    remainder = num1 % num2
    print("The remainder when", num1, "is divided by", num2, "is:", remainder)
else:
    print("Error: Division by zero is not allowed.")
