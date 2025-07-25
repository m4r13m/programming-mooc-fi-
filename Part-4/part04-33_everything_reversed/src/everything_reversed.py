def everything_reversed(l):
    reversed_list = []
    i = len(l) - 1
    while i >= 0:
        reversed_list.append(l[i][::-1])
        i -= 1

    return reversed_list


if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)