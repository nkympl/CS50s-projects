# Continue to ask the user for a couple of numbers 
# assuming it can use a float number and use round() function

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x / y, 2) # rounding to the nearest number of 2 digits
print(z)