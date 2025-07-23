last = ""
sentence = ""
while True:
    word = input("Please type in a word:")
    if word == last or word == "end":
        break
    last = word
    sentence += word+ " "
print(sentence)