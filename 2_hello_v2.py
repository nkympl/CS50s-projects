"""
first:
remind
that this is
a multiple line
comment in python
"""

# Introducing the concept of variables:
# Ask user for their name
name = input("What's your name? ")

# Now, remove a possible whitespace from str and capitalize user's name
name = name.strip().title() # Recall that a str comes with quite a few methods

# Say hello to user
print("Hello,", name)

# Another way of concatenate a value of variable (f-string)
# print(f"hello, {name}")

# Test of print function paramaters 
"""
print("Read documentation, ", end="")
print(name)
print("hello,", name, sep="???")
"""