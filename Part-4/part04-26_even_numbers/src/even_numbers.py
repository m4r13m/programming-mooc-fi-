def even_numbers(l):
    evens = []
    for n in l:
        if n % 2 == 0:
            evens.append(n)
    return evens

    
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)