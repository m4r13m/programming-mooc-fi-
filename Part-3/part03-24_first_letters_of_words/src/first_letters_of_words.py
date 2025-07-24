sentence = input("Please type in a sentence: ")
print(sentence[0])
i = 0
while i < len(sentence):
    if sentence[i] == " ":
        print(sentence[i+1])
    i += 1