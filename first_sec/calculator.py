print("hello myself")# Basic calculator program in Python

# Define a function to perform the calculation
def calculate(num1, num2, operator):
  if operator == '+':
    return num1 + num2
  elif operator == '-':
    return num1 - num2
  elif operator == '*':
    return num1 * num2
  elif operator == '/':
    return num1 / num2
  else:
    return "Invalid operator"

# Prompt the user to enter two numbers and an operator
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
operator = input("Enter an operator (+, -, *, /): ")

# Call the calculate function and print the result
result = calculate(num1, num2, operator)
print(result)
# #----------------------------------------------------------------------------------------------------------------------------
