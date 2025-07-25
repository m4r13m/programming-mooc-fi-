def most_common_character(word):
    c = 0
    for char in word:
        if word.count(char) > c:
            c = word.count(char)
    for char in word:
        if c == word.count(char):
            return char


if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))