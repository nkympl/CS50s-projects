# Continue to ask the user for a couple of numbers 
# assuming it can use a float number and use f-strings to specify how many digits you want the result to have

x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

print(f"{z:.2f}")