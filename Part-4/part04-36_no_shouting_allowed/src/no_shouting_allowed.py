def no_shouting(l):
    s = []
    for word in l:
        if word.isupper() == False:
            s.append(word)
    return s
        


if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)