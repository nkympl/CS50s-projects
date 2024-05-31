# It's time to define (and understand) a main() function.
# A main() function contains the main logic of my program.

def main(): # contains the main logic of the program.
    name = input("What's your name? ")
    hello(name)

def hello(to="stranger"): # contains a helper function to say hello.
    print("Hello,", to)

main()