def all_the_longest(l):
    longs = []
    long = len(l[0])
    for word in l:
        if len(word) > long:
            long = len(word)

    for w in l:
        if len(w) == long:
            longs.append(w)
    return longs

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']