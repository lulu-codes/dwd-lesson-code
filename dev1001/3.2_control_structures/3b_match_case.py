# Match-Case Statement in Python
# match-case statement is Python's version of a switch-case found in other languages.
# It allows us to match a variable's value against a set of patterns.

# --- USE: match-case Statement ---
http_status_code = 201 # Try 200, 500, 999
status_meaning = ""

# if http_status_code == 200:
#     status_meaning = "OK"
# elif http_status_code = 403:
#     status_meaning = "Forbidden"
# ...
match http_status_code:
    case 200 | 201:     # match-case (3b): How could you make case 200 and case 201 (Created) both lead to a similar "Success" message, perhaps by setting a common variable or using |? (e.g., case 200 | 201: status_type = "Success")
        status_meaning = "OK - Request successful."
    case 301:           # match-case (3b): Add a new case for http_status_code 301 that sets status_meaning to "Moved Permanently - Resource has a new URL."
        status_meaning = "Moved Permanently - Resource has a new URL."
    case 403:
        status_meaning = "Forbidden - You don't have permission."
    case 404:
        status_meaning = "Not Found - The resource doesn't exist."
    case 500:
        status_meaning = "Internal Server Error - Something went wrong on our end."
    case _: # Default case
        status_meaning = "Unknown or unhandled status code."


# match http_status_code:
#     case 200 | 201:
#         status_meaning = "OK - Request successful."
#     case _:
#         status_meaning = "Unsuccessful"

print(f"Status {http_status_code}: {status_meaning}")