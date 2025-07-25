l = []
i = 1
while True:
    print(f"The list is now {l}")
    option = input("a(d)d, (r)emove or e(x)it: ")
    if option == "x":
        print("Bye!")
        break
    elif option == "d":
        l.append(i)
        i += 1
    elif option == "r":
        i -= 1
        l.remove(i)
    
