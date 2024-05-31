"""
Create a hello function to take a >>paramater<< and use
the value of that parameter to plug into print
"""

def hello(to):
    print("Hello,", to)

name = input("What's your name? ")
hello(name)