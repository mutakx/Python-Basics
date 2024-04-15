# This is a one line comment.

#Basic operations
print(6-5)
print(5-6)
print(6+5)
# Will not eliminate the float reminder
print(11/2)
# Will eliminate the float reminder.
print(11//2) 
print(6*5)
# Also can be used to calculate using multiple operators.
# Using the BODMAS rule.
print(3+11*2)
print(3/2+1)

# Operations can also be done seperately using Brackets.
print((3+11)*2)

# Using the empercent sign/modulus,  this is help to get only the reminder.
print(11%2)
print(10%2)

# Adding a number to a string we have to convert the number to string.
print("Thor" + str(5))
#With space
print("Thor " + str(5))

# Using the absolute operator (converts to absolute number)
print(abs(-5))

# Using the return/Output

#Using the max & min operator
print(max(25, 9, -5, 10, -100))
print(min(25, 9, -5, 10, -100))

#Round operator (will only show the float value)
print(round(5.6))
print(round(5.5))
print(round(4.3))


#Function ceil (upper value) and floor (lower value) of the Math Library

#Declaration of Library. The asterix "*" represents everything of the library.

from math import *
print(floor(5.9))
print(ceil(5.1))

# Function Square Root.
print(sqrt(20))

