
# Program to divide two numbers

# Take input from the user
num1 = float(input("Enter the numerator: "))
num2 = float(input("Enter the denominator: "))

# Check for division by zero
if num2 != 0:
    quotient = num1 / num2
    print("The result of", num1, "divided by", num2, "is:", quotient)
else:
    print("Error: Division by zero is not allowed.")
