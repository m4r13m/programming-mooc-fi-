item = int(input("How many items: "))
l = []
i = 1
while i <= item:
    value = int(input(f"Item {i}:"))
    l.append(value)
    i += 1
print(l)

