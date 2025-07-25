def remove_smallest(my_list):
    small = my_list[0]
    for number in my_list:
        if number < small:
            small = number

    for n in my_list:
        if n == small:
            my_list.remove(n)


if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)