l = [1,2,3,4,5]
while True:
    i = int(input("Index: "))
    if i < 0:
        break
    value = int(input("Value: "))
    l[i] = value
    print(l)


