def first_word(sentence):
    i = sentence.find(" ")
    return sentence[0:i]

def second_word(sentence):
    i = sentence.count(" ")
    j = sentence.find(" ")
    if i == 1:
        return sentence[j + 1: ]
    l = j + 1
    while l < len(sentence):
        if sentence[l] == " ":
            break
        l += 1
    return sentence[j + 1: l]
    
def last_word(sentence):
    i = len(sentence) - 1
    while i >= 0:
        if sentence[i] == " ":
            return sentence[i+1:]
        i -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))