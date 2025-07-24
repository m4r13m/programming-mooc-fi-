word = input("Please type in a string:")
sub = input("Please type in a substring: ")
i = word.find(sub)
j = word[i+len(sub):].find(sub)
if j < 0:
    print("The substring does not occur twice in the string.")
else:
    print(f"The second occurrence of the substring is at index {j + i + len(sub)}.")