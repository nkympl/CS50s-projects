# Create a function to use the concept of "return value" to plug in a value inside another previous function.

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

main()