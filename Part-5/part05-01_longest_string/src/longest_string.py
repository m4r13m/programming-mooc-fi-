def longest(words):
    long = len(words[0])
    for word in words:
        if long < len(word):
            long = len(word)
    for w in words:
        if len(w) == long:
            return w

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))