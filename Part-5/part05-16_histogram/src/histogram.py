def histogram(word):
    w = {}
    for c in word:
        if c in w:
            continue
        w[c] = word.count((c))
    for key, value in w.items():
        print(key+" "+value* "*")

if __name__ =="__main__":
    histogram("statistically")
    histogram("abba")
