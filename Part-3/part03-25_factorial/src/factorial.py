while True:
    n = int(input("Please type in a number:"))
    if n <= 0:
        print("Thanks and bye!")
        break
    f = 1
    i = 1
    while i <= n:
        f *= i
        i += 1
    print(f"The factorial of the number {n} is {f}")