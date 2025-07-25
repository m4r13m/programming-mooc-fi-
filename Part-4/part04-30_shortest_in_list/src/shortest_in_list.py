def shortest(l):
    short = len(l[0])
    for word in l:
        if len(word) < short:
            short = len(word)

    for w in l:
        if len(w) == short:
            return w


if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = shortest(my_list)
    print(result)