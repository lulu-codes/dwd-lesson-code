# CREATE: event_planner.py
# Ask the user for the name of an event (e.g., "Birthday Party").
# Ask for the number of adult guests (integer).
# Ask for the number of child guests (integer).
# Assume adult tickets cost $25.75 each and child tickets cost $12.50 each.
# Calculate the total cost for adult tickets and child tickets separately.
# Calculate the overall total cost for the event.
# Print a summary using f-strings, formatting all costs to two decimal places. Include the event name and guest counts in the summary.
# Example output snippet:
# Event: Birthday Party
# Adult Guests: 10, Child Guests: 5
# Cost for Adults: $257.50
# Cost for Children: $62.50
# Total Event Cost: $320.00

event_name = str(input('Enter the name of your event: '))
adult_guests = int(input('Enter the number of adult guests: '))
child_guests = int(input('Enter the number of child guests: '))
adult_ticket = 25.75
child_ticket = 12.50
adults_cost = float(adult_guests * adult_ticket)
children_cost = float(child_guests * child_ticket)
total_event_cost = float(adults_cost + children_cost)

print(f'Event: {event_name}')
print(f'Adult Guests: {adult_guests}, Child Guests: {child_guests}')
print(f'Cost for Adults: ${adults_cost:.2f}')
print(f'Cost for Children: ${children_cost:.2f}')
print(f'Total Event Cost: ${total_event_cost:.2f}')