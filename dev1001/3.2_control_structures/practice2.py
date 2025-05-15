x = int(input("Enter a number between 1 and 7: "))

match xxx:
    case 1:
        x = "Monday"
    case 2:
        x = "Tuesday"
    case 3:
        x = "Wednesday"
    case 4:
        x = "Thursday"
    case 5:
        x = "Friday"
    case 6:
        x = "Saturday"
    case 7:
        x = "Sunday"

print(f"The day of the week is: {x}")