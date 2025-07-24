word = input("Please type in a word:")
char = input("Please type in a character:")
i = word.find(char)
if i >= 0 and i < len(word) - 2:
    print(word[i: i+3])