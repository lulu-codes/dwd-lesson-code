# Lists Exercise

# Shopping Cart
cart = ["apples", "bananas", "bread"]

# 1. Add milk to the end of the cart.
cart.append("milk")
print(f"Appended 'milk': {cart}")

# 2. Bananas are out of stock. Remove them.
cart.remove("bananas")
print(f"Removed 'bananas': {cart}")

# 3. You remembered you need eggs and they're a higher priority
#       than everything other than apples.
#       Insert eggs right after apples.
cart.insert(1, "eggs")
print(f"Inserted: {cart}")
# 4. You decide to get 2 more apples, so add them.
cart.extend(['apples', 'apples'])
print(f"Extended: {cart}")
# 5. Print out how many apples are in the cart.
print(f"Number of apples: {cart.count('apples')}")
# 6. Sort the cart alphabetically.
cart.sort()
# 7. Get and print a new list with only the first 2 items.
print(cart[:2])
# 8. Get and print a new list with all items EXCEPT the first one.
print(cart[1:])
# 9. Print the final cart and how many items are in it.
print(cart)
print(f"Total items: {len(cart)}")
