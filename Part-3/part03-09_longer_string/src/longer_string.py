w1 = input("Please type in string 1:")
w2 = input("Please type in string 2: ")
if len(w1) > len(w2):
    print(f"{w1} is longer")
elif len(w1) < len(w2):
    print(f"{w2} is longer")
else:
    print("The strings are equally long")