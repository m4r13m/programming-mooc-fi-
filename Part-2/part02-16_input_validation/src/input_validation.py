from math import sqrt
# Write your solution here
while True:
    n = int(input("Please type in a number: "))
    if n < 0:
        print("Invalid number")
    elif n > 0:
        print(sqrt(n))
    else:
        print("Exiting...")
        break