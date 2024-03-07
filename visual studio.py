def calculate(num1, num2, operator):
  """
  Performs the specified arithmetic operation on two numbers.

  Args:
      num1: The first number.
      num2: The second number.
      operator: The arithmetic operator (+, -, *, /).

  Returns:
      The result of the operation.

  Raises:
      ValueError: If the operator is invalid or division by zero is attempted.
  """
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    if num2 == 0:
      raise ValueError("Division by zero is not allowed")
    return num1 / num2
  else:
    raise ValueError("Invalid operator")

while True:
  # Get user input
  try:
    num1 = float(input("Enter first number: "))
    operator = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
  except ValueError:
    print("Invalid input. Please enter numbers only.")
    continue

  # Perform calculation
  try:
    result = calculate(num1, num2, operator)
  except ValueError as e:
    print(e)
    continue

  # Display result
  print(f"{num1} {operator} {num2} = {result}")

  # Ask if user wants to perform another calculation
  choice = input("Do you want to perform another calculation? (yes/no): ")
  if choice.lower() != "yes":
    break

print("Calculator closed.")
