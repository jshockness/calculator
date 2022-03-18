# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide
def divide(n1, n2):
  return n1 / n2

# Dictionary of Operations
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

# Ask for numbers
num1 = int(input("What's the first number: "))
# Loop through operations
for symbol in operations:
  print(symbol)
operation_symbol = input("Pick an operation from the selection above: ")
num2 = int(input("What's the second number: "))
# Get the operation symbol from operations
calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")

operation_symbol = input("Pick another operation: ")
num3 = int(input("What's the next number: "))
calculation_function = operations[operation_symbol]
second_answer = calculation_function(calculation_function(num1, num2), num3)

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")