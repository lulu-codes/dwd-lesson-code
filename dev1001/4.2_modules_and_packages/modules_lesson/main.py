#main.py

import stuff.functions

import stuff.functions as funky
# # import sys
# # As paths can get quite long, Python allows us to create an alias or a namespace that we want to use when referring to the module in our code.
# # We just have to use the as keyword. By assigning the import an alias of funky we can use that as our namespace when referring to the module in our code!
# print("And the answer to the equation is….")
# # answer = stuff.functions.sum(3, 6)
answer = funky.sum(3, 6)
print(answer)

# print("The paths that Python looks for modules is….")
# print(sys.path)

# import stuff.functions as funky
# print("And the answer to the equation is….")
# answer = funky.sum(3, 6)
# print(answer)


# If we want to straight up import the sum function and be able to call it with sum( )?
# Remember Python doesn’t do that automatically because it doesn’t know which one you’d want to keep if you had your own sum function in main.py
# but if we are explicit about what we want to import from a module Python will allow it.
# Here we have explicitly told Python that all we want from the functions.py file is the function sum.
# Because of that Python will import the sum function definition directly into our main.py without a namespace!
# This does have the possibility of things going wrong because you accidentally use the wrong one so be careful when you do this.

from stuff.functions import sum

print("And the answer to the equation is….")
answer = sum(3, 6)
print(answer)