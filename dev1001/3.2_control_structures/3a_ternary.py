# Ternary Conditional Statement in Python
# A ternary conditional statement is a compact way to write an if-else condition in a single line.
# It’s sometimes called a "conditional expression."

# --- USE: Ternary Operator ---
age = 13

# Ternary flow
# 1. Python evaluates the boolean expression between 'if' and 'else'
# 2. If TRUE, the whole ternary expression evaluates to whatever is on the left of the 'if'
# 3. Otherwise, it evaluates to whatever is to the right of the 'else'

# Ternary (3a): Rewrite the ternary assignment for category using a traditional if-else block to demonstrate equivalence.
# Then, change the condition in the ternary operator: if age < 13, category is "Child", else it's "Teen or Adult".
category = "Adult" if age >= 18 else "Minor" # The ternary operator
print(f"Age: {age}, Category: {category}")

# Ternary (3a): Rewrite the ternary assignment for category using a traditional if-else block to demonstrate equivalence.
# Then, change the condition in the ternary operator: if age < 13, category is "Child", else it's "Teen or Adult".
category = "Child" if age < 13 else "Teen or Adult" # The ternary operator
print(f"Age: {age}, Category: {category}")
