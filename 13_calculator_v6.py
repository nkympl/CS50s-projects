"""Introducing f-strings: they provide a powerful and flexible way to format strings in Python, enhancing both readability and performance. 
They are now the preferred method for string formatting in modern Python code.
"""

# Ask the user for a couple of numbers but now assume it can use a float number

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)
print(f"{z:,}") # format the number to USA 3 digits pattern