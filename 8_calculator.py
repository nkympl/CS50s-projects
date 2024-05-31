# Ask the user a couple of numbers

x = input("What's x? ")
y = input("What's y? ")

# The tricky point here is that input() only works if the answer is a str.
# If I want to make a calculator, I'll need numbers and for that I'll use int() to convert the str.

z = int(x) + int(y)
print(z)

# This might not be the best way to build my calculator program, how can I improve that?
# See further versions!