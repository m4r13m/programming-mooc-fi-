def palindromes(word):
    if word == word[::-1]:
        return True
    return False

while True:
    w = input("Please type in a palindrome: ")
    if palindromes(w):
        print(f"{w} is a palindrome!")
        break
    print("that wasn't a palindrome")

# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
