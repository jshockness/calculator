from art import logo

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

# Calculator Function
def calculator():
  print(logo)
  # Ask for numbers
  num1 = float(input("What's the first number: "))
  # Loop through operations
  for symbol in operations:
    print(symbol)
  # create while loop to check if user wants to proceed.
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Pick an operation from the selection above: ")
    num2 = float(input("What's the second number: "))
    # Get the operation symbol from operations
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
  
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to end calculation: ") == "y":
      num1 = answer
    else:
      should_continue = False
      if input("Type 'y' if you like to calculate new numbers?  or 'n' to exit") == "y":
        calculator()

calculator()