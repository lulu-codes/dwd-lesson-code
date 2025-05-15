xxx = int(input("Enter a number between 1 and 7: "))
day = ""

match xxx:
    case 1:
        day = "Monday"
    case 2:
        day = "Tuesday"
    case 3:
        day = "Wednesday"
    case 4:
        day = "Thursday"
    case 5:
        day = "Friday"
    case 6:
        day = "Saturday"
    case 7:
        day = "Sunday"

print(f"The day of the week is: {day}")