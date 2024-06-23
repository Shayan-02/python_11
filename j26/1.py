def sum_digits(n):
  """
  This function takes an integer n and returns the sum of its digits.
  """
  sum = 0
  while n > 0:
    sum += n % 10
    n //= 10
  return sum

# Get the input from the user
numbers = []
for i in range(5):
  number = int(input(f"Enter number {i+1}: "))
  numbers.append(number)

# Find the numbers whose sum of digits is divisible by 13
divisible_numbers = []
for number in numbers:
  if sum_digits(number) % 13 == 0:
    divisible_numbers.append(number)

# Print the results
print("Numbers whose sum of digits is divisible by 13:")
for number in divisible_numbers:
  print(number, end=" ")