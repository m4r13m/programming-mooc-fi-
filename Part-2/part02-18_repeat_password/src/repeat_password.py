password = input("Password: ")
while True:
    rpass = input("Repeat password: ")
    if password == rpass:
        print("User account created!")
        break
    print("They do not match!")