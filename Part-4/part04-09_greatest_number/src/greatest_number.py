# Write your solution here
def greatest_number(x, y, z):
    if x <= z and y <= z:
        return z
    elif x <= y and z <= y:
        return y
    else:
        return x

# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)
    print(greatest_number(3, 4, 1)) # 4
    print(greatest_number(99, -4, 7)) # 99
    print(greatest_number(0, 0, 0)) # 0