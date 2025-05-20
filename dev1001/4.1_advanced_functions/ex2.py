# Callbacks Exercise
#
# 1. Write a function: perform_operation(a, b, math_callback).
def perform_operation(a, b, math_callback):
    result = math_callback(a, b)
    print(f"Result: {result}")

def add_them(a, b):
    return a + b
def multiply_them(a, b):
    return a * b

perform_operation(5, 3, add_them)
perform_operation(5, 3, multiply_them)

# 2. This function should take two numbers and a callback.
# 3. The callback function itself should accept two numbers and return their result
# 4. perform_operation() should then print this result.
# 5. Create two simple callbacks (e.g., add_them, multiply_them) and
#       test perform_operation with both.

