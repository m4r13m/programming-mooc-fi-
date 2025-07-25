def distinct_numbers(l):
    d = []
    for n in l:
        if n not in d:
            d.append(n)

    return sorted(d)

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]