def no_vowels(word):
    for c in word:
        if c in ["a","e","u","i","o"]:
            word = word.replace(c, "")
    return word

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))