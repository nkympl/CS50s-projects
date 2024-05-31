"""
Now take the previous code and create a hello function to get
a parameter with a default value
"""

def hello(to="stranger"):
    print("Hello,", to)

hello()

name = input("What's your name? ")
hello(name)