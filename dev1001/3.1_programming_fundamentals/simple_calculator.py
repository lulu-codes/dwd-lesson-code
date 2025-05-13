# CREATE: simple_calculator.py
# Ask the user to enter a whole number.
# Ask the user to enter another whole number.
# Convert both inputs to integers and store them in variables.
# Calculate and print the sum of the two numbers.
# Calculate and print the product (multiplication) of the two numbers.
# Example Output:
# Enter first number: 10
# Enter second number: 5
# Sum: 15
# Product: 50

first_number = int(input('Enter a whole number: '))
second_number = int(input('Enter another whole number: '))
sum = first_number + second_number
print(f'Sum: {sum}')
product = first_number * second_number
print(f'Product: {product}')