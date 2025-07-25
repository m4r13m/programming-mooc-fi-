def double_items(my_list):
    doubled = my_list[:]
    for i in range(len(doubled)):
        doubled[i] *= 2
    return doubled

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)