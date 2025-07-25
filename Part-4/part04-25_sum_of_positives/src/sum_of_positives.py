def sum_of_positives(l):
    s = 0
    for n in l:
        if n > 0:
            s += n
    return s


if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)