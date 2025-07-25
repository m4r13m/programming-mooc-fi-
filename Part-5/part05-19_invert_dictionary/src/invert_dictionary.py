def invert(d):
    keys = []
    values = []
    for key, value in d.items():
        keys.append(key)
        values.append(value)
    d.clear()

    for i in range(len(keys)):
        d[values[i]] = keys[i]


if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)