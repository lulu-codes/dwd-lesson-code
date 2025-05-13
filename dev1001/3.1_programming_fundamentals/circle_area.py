# CREATE: circle_area.py
# Define a variable pi and assign it the value 3.14159.
# Ask the user to enter the radius of a circle (allow decimals).
# Calculate the area: area = pi * radius * radius.
# Print the radius and the calculated area, formatted to 3 decimal places.
# Example output:
# A circle with radius [Radius] has an area of [Area].

pi = 3.14159
radius = float(input('Enter the radius of a circle: '))
area = pi * radius * radius
print(f'A circle with radius {radius} has an area of {area:.3f}.')