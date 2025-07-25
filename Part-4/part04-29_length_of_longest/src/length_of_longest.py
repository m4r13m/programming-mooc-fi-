def length_of_longest(l):
    long = len(l[0])
    for word in l:
        if long < len(word):
            long = len(word)
    return long

    
if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = length_of_longest(my_list)
    print(result)