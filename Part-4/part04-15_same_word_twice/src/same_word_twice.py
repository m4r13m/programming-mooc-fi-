words = []
c = 0
while True:
    word = input("Word: ")
    if word in words:
        break
    c += 1
    words.append(word)

print(f"You typed in {c} different words")
